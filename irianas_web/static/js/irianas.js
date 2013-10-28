jQuery(document).ready(function($) {
    $('#time_button').click(time_expand);

    if($IP_CLIENT){
        $('#update_system').click(update_system);
        services_info();
        system_monitor();
        events();
        client_ifo();
        setInterval("system_monitor()", 5000);
        setInterval("services_info()", 10000);
        setInterval("events()", 10000);

    }
    time_session();
    setInterval("time_session()", 30000);
});


function client_ifo(){
    // System Info
    jQuery(document).ready(function($) {
        $.ajax({
            type: "GET",
            url: $SCRIPT_ROOT + '/client/info/' + $IP_CLIENT,
            async: true,
            dataType: "json",
            error: function(XMLHttpRequest, textStatus, errorThrown) {
                $('#client-loading').hide();
                $('#client-error').show();
            },
            success: function(data){
                $('#client-loading').hide();
                $('#client-error').hide();

                // HOSTNAME
                $('#client-hostname').text(data.host_name);

                // Operating System
                $('#client-os').text(data.os);

                // Architecture
                $('#client-arch').text(data.arch);

                // Memory
                $('#client-memory').text((data.memory / (1024 * 1024)) + " MB");

                $("#client-info").show();
            }
        });
    });
}

// Services Info
function services_info () {
    jQuery(document).ready(function($) {
        $.ajax({
            type: "GET",
            url: $SCRIPT_ROOT + '/client/services/' + $IP_CLIENT,
            async: true,
            dataType: "json",
            error: function(XMLHttpRequest, textStatus, errorThrown) {
                $('#services-loading').hide();
                $("#services").hide();
                $('#services-error').show();
            },
            success: function(data){
                $('#services-error').hide();
                $('#services-loading').hide();

                $.each(data, function(index, value) {
                    var ser_status = '#' + index + '-status';
                    var ser_status_button = '#' + index + '-status-button';
                    var ser_installed_button = '#' + index + '-installed-button';
                    var url_service = '/client/services/' + index;
                    if(value.status){
                        $(ser_status).text('ON');

                        $(ser_status_button).show();
                        $(ser_status_button).text('Apagar');
                        $(ser_status_button).removeClass('btn-success');
                        $(ser_status_button).addClass('btn-danger');
                        $(ser_status_button).attr("href", url_service + '/stop/' + $IP_CLIENT);
                        $(ser_status_button).unbind('click', send_action).click(send_action);

                        $(ser_installed_button).text('Remover');
                        $(ser_installed_button).removeClass('btn-success');
                        $(ser_installed_button).addClass('btn-danger');
                        $(ser_installed_button).attr("href", url_service + '/remove/' + $IP_CLIENT);
                        $(ser_installed_button).unbind('click', send_action).click(send_action);
                    }else{
                        $(ser_status).text('OFF');
                        if(value.status_service){
                            $(ser_status_button).show();
                            $(ser_status_button).text('Encender');
                            $(ser_status_button).removeClass('btn-danger');
                            $(ser_status_button).addClass('btn-success');
                            $(ser_status_button).attr("href", url_service + '/start/' + $IP_CLIENT);
                            $(ser_status_button).unbind('click', send_action).click(send_action);

                            $(ser_installed_button).text('Remover');
                            $(ser_installed_button).removeClass('btn-primary');
                            $(ser_installed_button).addClass('btn-danger');
                            $(ser_installed_button).attr("href", url_service + '/remove/' + $IP_CLIENT);
                            $(ser_installed_button).unbind('click', send_action).click(send_action);
                        }else{
                            $(ser_status).text('NO INSTALADO');
                            $(ser_status_button).hide();
                            $(ser_installed_button).text('Instalar');
                            $(ser_installed_button).removeClass('btn-danger');
                            $(ser_installed_button).addClass('btn-primary');
                            $(ser_installed_button).attr("href", url_service + '/install/' + $IP_CLIENT);
                            $(ser_installed_button).unbind('click', send_action).click(send_action);
                        }
                    }
                });

                $("#services").show();
            }
        });
    });
}


function system_monitor(){
    // Monitor
    jQuery(document).ready(function($) {
        $.ajax({
            type: "GET",
            url: $SCRIPT_ROOT + '/client/monitor/' + $IP_CLIENT,
            async: true,
            dataType: "json",
            error: function(XMLHttpRequest, textStatus, errorThrown) {
                $('#monitor-loading').hide();
                $("#monitor").hide();
                $('#monitor-error').show();
            },
            success: function(data){
                $('#monitor-loading').hide();
                $('#monitor-error').hide();

                // CPU
                $('#monitor-cpu').width(data.cpu + "%");
                $('#monitor-cpu-h5').text(data.cpu + "% CPU");

                // Memory
                $('#monitor-memory').width(data.memory + "%");
                $('#monitor-memory-h5').text(data.memory + "% Memoria");

                // Disk
                $('#monitor-disk').width(data.disk + "%");
                $('#monitor-disk-h5').text(data.disk + "% Disco");

                $("#monitor").show();
            }
        });
    });
}

function send_action (event) {
    $.ajax({
        type: "GET",
        url: $( this ).attr("href"),
        async: true,
        dataType: "json",
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            bootbox.alert("Error al procesar la solicitud.");
        },
        success: function(data){
            bootbox.alert("Solicitud enviada.");
        }
    });
    event.preventDefault();
    event.stopPropagation();
}

function events () {
    $.ajax({
        type: "GET",
        url: $SCRIPT_ROOT + '/client/events/' + $IP_CLIENT,
        async: true,
        dataType: "json",
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            $('#events-loading').hide();
            $('#events-content').hide();
            $('#events-error').show();
        },
        success: function(data){
            var html = '';
            $.each(data, function(index, value) {
                html += '<div class="alert alert-info"><strong>' + value + '</strong> (' + index + ')</div>';
            });

            $('#events-content').html(html);

            $('#events-loading').hide();
            $('#events-error').hide();
            $('#events-content').show();
        }
    });
}

function time_session () {
    $.ajax({
        type: "GET",
        url: $SCRIPT_ROOT + '/time/',
        async: true,
        dataType: "json",
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            var msg = 'Sesi&oacute;n finalizada';

            $('#time_user').html(msg);
        },
        success: function(data){
            var msg = 'Tiempo restante en la sesi&oacute;n: ' + data.time;

            $('#time_user').html(msg);
        }
    });
}

function time_expand (event) {
    $.ajax({
        type: "POST",
        url: $SCRIPT_ROOT + '/time/',
        async: true,
        dataType: "json",
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            bootbox.alert("Error al procesar la solicitud.");
        },
        success: function(data){
            if(data.status){
                bootbox.alert("Solicitud enviada.");
            }else{
                bootbox.alert("No se puede procesar esta solicitud. Tiempo M&aacute;ximo 30 min.");
            }
        }
    });
    event.preventDefault();
    event.stopPropagation();
}

function update_system (event) {
    $.ajax({
        type: "GET",
        url: $SCRIPT_ROOT + '/client/update/' + $IP_CLIENT,
        async: true,
        dataType: "json",
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            bootbox.alert("Error al procesar la solicitud.");
        },
        success: function(data){
            bootbox.alert("Solicitud enviada.");
        }
    });
    event.preventDefault();
    event.stopPropagation();
}
