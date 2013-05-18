(function() {
    $(document).ready(function() {
        var d, date, m, metrics, newOrders, orders, plot, randNumber, randSmallerNumber, theme, y;

        if (Modernizr.localstorage) {
            theme = localStorage.getItem("theme");
            if (theme !== null) {
                $("body").removeClass().addClass(theme);
            }
        }
        $(".change-color-to-red").hover(function() {
            $("body").removeClass();
            return localStorage.setItem("theme", null);
        });
        $(".change-color-to-blue").hover(function() {
            $("body").removeClass();
            $("body").addClass("blue-theme");
            return localStorage.setItem("theme", "blue-theme");
        });
        $(".change-color-to-orange").hover(function() {
            $("body").removeClass();
            $("body").addClass("orange-theme");
            return localStorage.setItem("theme", "blue-theme");
        });
        $(".change-color-to-green").hover(function() {
            $("body").removeClass();
            $("body").addClass("green-theme");
            return localStorage.setItem("theme", "green-theme");
        });
        $(".change-color-to-purple").hover(function() {
            $("body").removeClass();
            $("body").addClass("purple-theme");
            return localStorage.setItem("theme", "purple-theme");
        });
        $(".fullfill-items").click(function() {
            return confirm("Yay! Do you really want to fullfil selected items?");
        });
        $(".data-table").dataTable({
            sDom: "<'row-fluid'<'span6'l><'span6 text-right'f>r>t<'row-fluid'<'span6'i><'span6 text-right'p>>",
            sPaginationType: "bootstrap",
            oLanguage: {
                sLengthMenu: "_MENU_ records per page"
            }
        });
        $("#check-all").click(function() {
            return $(this).parents("table:eq(0)").find(".only-checkbox :checkbox").attr("checked", this.checked);
        });
        $(".box-refresh").click(function(e) {
            alert("Your refresh action.");
            return e.preventDefault();
        });
        $(".box-remove").click(function(e) {
            var box;

            box = $(this).parents(".box");
            box.fadeOut(300, function() {
                return $(this).remove();
            });
            return e.preventDefault();
        });
        $(".alert-example").click(function() {
            return alert("Hey there!");
        });
        $(".alert-example-original").click(function() {
            return _originalAlert("Hey there!");
        });
        $(".popover-top").popover({
            placement: "top",
            container: "body",
            trigger: "hover"
        });
        $(".popover-bottom").popover({
            placement: "bottom",
            container: "body",
            trigger: "hover"
        });
        $(".popover-left").popover({
            placement: "left",
            container: "body",
            trigger: "hover"
        });
        $(".popover-right").popover({
            placement: "right",
            container: "body",
            trigger: "hover"
        });
        $(".tooltip-top").tooltip({
            placement: "top",
            container: "body"
        });
        $(".tooltip-bottom").tooltip({
            placement: "bottom",
            container: "body"
        });
        $(".tooltip-left").tooltip({
            placement: "left",
            container: "body"
        });
        $(".tooltip-right").tooltip({
            placement: "right",
            container: "body"
        });
        $('.messenger-top-right').click(function() {
            Messenger().hideAll();
            Messenger.options = {
                extraClasses: 'messenger-fixed messenger-on-top messenger-on-right',
                theme: 'block'
            };
            return Messenger().post({
                message: "Yahooooo!",
                hideAfter: 5,
                type: 'error',
                hideOnNavigate: true
            });
        });
        $('.messenger-top-center').click(function() {
            Messenger.options = {
                extraClasses: 'messenger-fixed messenger-on-top',
                theme: 'block'
            };
            return Messenger().post({
                message: "Yahooooo!",
                hideAfter: 5,
                type: 'error',
                hideOnNavigate: true
            });
        });
        $('.messenger-top-left').click(function() {
            Messenger.options = {
                extraClasses: 'messenger-fixed messenger-on-top messenger-on-left',
                theme: 'block'
            };
            return Messenger().post({
                message: "Yahooooo!",
                hideAfter: 5,
                type: 'error',
                hideOnNavigate: true
            });
        });
        $('.messenger-top-block').click(function() {
            Messenger.options = {
                extraClasses: "messenger-fixed messenger-on-top",
                theme: "block"
            };
            return Messenger().post({
                message: "Yahooooo!",
                hideAfter: 5,
                hideOnNavigate: true
            });
        });
        $('.messenger-bottom-right').click(function() {
            Messenger.options = {
                extraClasses: 'messenger-fixed messenger-on-bottom messenger-on-right',
                theme: 'block'
            };
            return Messenger().post({
                message: "Yahooooo!",
                hideAfter: 5,
                type: 'error',
                hideOnNavigate: true
            });
        });
        $('.messenger-bottom-center').click(function() {
            Messenger.options = {
                extraClasses: 'messenger-fixed messenger-on-bottom',
                theme: 'block'
            };
            return Messenger().post({
                message: "Yahooooo!",
                hideAfter: 5,
                type: 'error',
                hideOnNavigate: true
            });
        });
        $('.messenger-bottom-left').click(function() {
            Messenger.options = {
                extraClasses: 'messenger-fixed messenger-on-bottom messenger-on-left',
                theme: 'block'
            };
            return Messenger().post({
                message: "Yahooooo!",
                hideAfter: 5,
                type: 'error',
                hideOnNavigate: true
            });
        });
        $('.messenger-bottom-block').click(function() {
            Messenger.options = {
                extraClasses: "messenger-fixed messenger-on-bottom",
                theme: "block"
            };
            return Messenger().post({
                message: "Yahooooo!",
                hideAfter: 5,
                hideOnNavigate: true
            });
        });
        $("#datetimepicker").datetimepicker();
        $("#datepicker").datetimepicker({
            pickTime: false
        });
        $("#timepicker").datetimepicker({
            pickDate: false
        });
        $("#daterange").daterangepicker({
            ranges: {
                Today: ["today", "today"],
                Yesterday: ["yesterday", "yesterday"],
                "Last 7 Days": [
                    Date.today().add({
                        days: -6
                    }), "today"
                ],
                "Last 30 Days": [
                    Date.today().add({
                        days: -29
                    }), "today"
                ],
                "This Month": [Date.today().moveToFirstDayOfMonth(), Date.today().moveToLastDayOfMonth()],
                "Last Month": [
                    Date.today().moveToFirstDayOfMonth().add({
                        months: -1
                    }), Date.today().moveToFirstDayOfMonth().add({
                        days: -1
                    })
                ]
            }
        }, function(start, end) {
            return $("#daterange span").html(start.toString('yyyy-MM-d') + ' - ' + end.toString('yyyy-MM-d'));
        });
        $(".daterange").daterangepicker({
            ranges: {
                Today: ["today", "today"],
                Yesterday: ["yesterday", "yesterday"],
                "Last 7 Days": [
                    Date.today().add({
                        days: -6
                    }), "today"
                ],
                "Last 30 Days": [
                    Date.today().add({
                        days: -29
                    }), "today"
                ],
                "This Month": [Date.today().moveToFirstDayOfMonth(), Date.today().moveToLastDayOfMonth()],
                "Last Month": [
                    Date.today().moveToFirstDayOfMonth().add({
                        months: -1
                    }), Date.today().moveToFirstDayOfMonth().add({
                        days: -1
                    })
                ]
            }
        }, function(start, end) {
            return console.log(start + " - " + end);
        });
        $(".select2").select2();
        $('.wysihtml5').wysihtml5();
        $(".colorpicker-hex").colorpicker({
            format: "hex"
        });
        $(".colorpicker-rgb").colorpicker({
            format: "rgb"
        });
        $(".mention").mention({
            users: [
                {
                    name: "Lindsay Made",
                    username: "LindsayM",
                    image: "http://placekitten.com/25/25"
                }, {
                    name: "Rob Dyrdek",
                    username: "robdyrdek",
                    image: "http://placekitten.com/25/24"
                }, {
                    name: "Rick Bahner",
                    username: "RickyBahner",
                    image: "http://placekitten.com/25/23"
                }, {
                    name: "Jacob Kelley",
                    username: "jakiestfu",
                    image: "http://placekitten.com/25/22"
                }, {
                    name: "John Doe",
                    username: "HackMurphy",
                    image: "http://placekitten.com/25/21"
                }, {
                    name: "Charlie Edmiston",
                    username: "charlie",
                    image: "http://placekitten.com/25/20"
                }, {
                    name: "Andrea Montoya",
                    username: "andream",
                    image: "http://placekitten.com/24/20"
                }, {
                    name: "Jenna Talbert",
                    username: "calisunshine",
                    image: "http://placekitten.com/23/20"
                }, {
                    name: "Street League",
                    username: "streetleague",
                    image: "http://placekitten.com/22/20"
                }, {
                    name: "Loud Mouth Burrito",
                    username: "Loudmouthfoods",
                    image: "http://placekitten.com/21/20"
                }
            ]
        });
        if ($("#validation").length !== 0) {
            metrics = [["#email", "presence", "Cannot be empty"], ["#email", "email", "Not valid email"], ["#number", "integer", "Not a number"], ["#presence", "presence", "Cannot be empty"], ["#password", "min-length:4", "At least 4 characters"], ["#password_confirmation", "same-as:#password", "Please enter same value"]];
            $("#validation").nod(metrics);
        }
        randNumber = function() {
            return ((Math.floor(Math.random() * (1 + 50 - 20))) + 20) * 800;
        };
        randSmallerNumber = function() {
            return ((Math.floor(Math.random() * (1 + 40 - 20))) + 10) * 200;
        };
        if ($("#stats-chart1").length !== 0) {
            orders = [[1, randNumber() - 10], [2, randNumber() - 10], [3, randNumber() - 10], [4, randNumber()], [5, randNumber()], [6, 4 + randNumber()], [7, 5 + randNumber()], [8, 6 + randNumber()], [9, 6 + randNumber()], [10, 8 + randNumber()], [11, 9 + randNumber()], [12, 10 + randNumber()], [13, 11 + randNumber()], [14, 12 + randNumber()], [15, 13 + randNumber()], [16, 14 + randNumber()], [17, 15 + randNumber()], [18, 15 + randNumber()], [19, 16 + randNumber()], [20, 17 + randNumber()], [21, 18 + randNumber()], [22, 19 + randNumber()], [23, 20 + randNumber()], [24, 21 + randNumber()], [25, 14 + randNumber()], [26, 24 + randNumber()], [27, 25 + randNumber()], [28, 26 + randNumber()], [29, 27 + randNumber()], [30, 31 + randNumber()]];
            newOrders = [[1, randSmallerNumber() - 10], [2, randSmallerNumber() - 10], [3, randSmallerNumber() - 10], [4, randSmallerNumber()], [5, randSmallerNumber()], [6, 4 + randSmallerNumber()], [7, 5 + randSmallerNumber()], [8, 6 + randSmallerNumber()], [9, 6 + randSmallerNumber()], [10, 8 + randSmallerNumber()], [11, 9 + randSmallerNumber()], [12, 10 + randSmallerNumber()], [13, 11 + randSmallerNumber()], [14, 12 + randSmallerNumber()], [15, 13 + randSmallerNumber()], [16, 14 + randSmallerNumber()], [17, 15 + randSmallerNumber()], [18, 15 + randSmallerNumber()], [19, 16 + randSmallerNumber()], [20, 17 + randSmallerNumber()], [21, 18 + randSmallerNumber()], [22, 19 + randSmallerNumber()], [23, 20 + randSmallerNumber()], [24, 21 + randSmallerNumber()], [25, 14 + randSmallerNumber()], [26, 24 + randSmallerNumber()], [27, 25 + randSmallerNumber()], [28, 26 + randSmallerNumber()], [29, 27 + randSmallerNumber()], [30, 31 + randSmallerNumber()]];
            plot = $.plot($("#stats-chart1"), [
                {
                    data: orders,
                    label: "Orders"
                }, {
                    data: newOrders,
                    label: "New rders"
                }
            ], {
                series: {
                    lines: {
                        show: true,
                        lineWidth: 3
                    },
                    shadowSize: 0
                },
                legend: {
                    show: false
                },
                grid: {
                    clickable: true,
                    hoverable: true,
                    borderWidth: 0,
                    tickColor: "#f4f7f9"
                },
                colors: ["#00acec", "#f8a326"]
            });
        }
        if ($("#stats-chart2").length !== 0) {
            orders = [[1, randNumber() - 5], [2, randNumber() - 6], [3, randNumber() - 10], [4, randNumber()], [5, randNumber()], [6, 4 + randNumber()], [7, 10 + randNumber()], [8, 12 + randNumber()], [9, 6 + randNumber()], [10, 8 + randNumber()], [11, 9 + randNumber()], [12, 10 + randNumber()], [13, 11 + randNumber()], [14, 12 + randNumber()], [15, 3 + randNumber()], [16, 14 + randNumber()], [17, 14 + randNumber()], [18, 15 + randNumber()], [19, 16 + randNumber()], [20, 17 + randNumber()], [21, 18 + randNumber()], [22, 19 + randNumber()], [23, 20 + randNumber()], [24, 21 + randNumber()], [25, 14 + randNumber()], [26, 24 + randNumber()], [27, 25 + randNumber()], [28, 26 + randNumber()], [29, 27 + randNumber()], [30, 31 + randNumber()]];
            newOrders = [[1, randSmallerNumber() - 10], [2, randSmallerNumber() - 10], [3, randSmallerNumber() - 10], [4, randSmallerNumber()], [5, randSmallerNumber()], [6, 4 + randSmallerNumber()], [7, 5 + randSmallerNumber()], [8, 6 + randSmallerNumber()], [9, 6 + randSmallerNumber()], [10, 8 + randSmallerNumber()], [11, 9 + randSmallerNumber()], [12, 10 + randSmallerNumber()], [13, 11 + randSmallerNumber()], [14, 12 + randSmallerNumber()], [15, 13 + randSmallerNumber()], [16, 14 + randSmallerNumber()], [17, 15 + randSmallerNumber()], [18, 15 + randSmallerNumber()], [19, 16 + randSmallerNumber()], [20, 17 + randSmallerNumber()], [21, 18 + randSmallerNumber()], [22, 19 + randSmallerNumber()], [23, 20 + randSmallerNumber()], [24, 21 + randSmallerNumber()], [25, 14 + randSmallerNumber()], [26, 24 + randSmallerNumber()], [27, 25 + randSmallerNumber()], [28, 26 + randSmallerNumber()], [29, 27 + randSmallerNumber()], [30, 31 + randSmallerNumber()]];
            plot = $.plot($("#stats-chart2"), [
                {
                    data: orders,
                    label: "Orders"
                }, {
                    data: newOrders,
                    label: "New orders"
                }
            ], {
                series: {
                    lines: {
                        show: true,
                        lineWidth: 3
                    },
                    shadowSize: 0
                },
                legend: {
                    show: false
                },
                grid: {
                    clickable: true,
                    hoverable: true,
                    borderWidth: 0,
                    tickColor: "#f4f7f9"
                },
                colors: ["#f34541", "#49bf67"]
            });
            $("#stats-chart2").bind("plotclick", function(event, pos, item) {
                if (item) {
                    return alert("Yeah! You just clicked on point " + item.dataIndex + " in " + item.series.label + ".");
                }
            });
        }
        $("#events .external-event").each(function() {
            var eventObject;

            eventObject = {
                title: $.trim($(this).text())
            };
            $(this).data("eventObject", eventObject);
            return $(this).draggable({
                zIndex: 999,
                revert: true,
                revertDuration: 0
            });
        });
        date = new Date();
        d = date.getDate();
        m = date.getMonth();
        y = date.getFullYear();
        $("#calendar").fullCalendar({
            editable: true,
            droppable: true,
            header: {
                left: '',
                center: 'prev,title,next',
                right: ''
            },
            drop: function(date, allDay) {
                var copiedEventObject, originalEventObject;

                originalEventObject = $(this).data("eventObject");
                copiedEventObject = $.extend({}, originalEventObject);
                copiedEventObject.start = date;
                copiedEventObject.allDay = allDay;
                $("#calendar").fullCalendar("renderEvent", copiedEventObject, true);
                if ($("#drop-remove").is(":checked")) {
                    return $(this).remove();
                }
            },
            events: [
                {
                    title: "All Day Event",
                    start: new Date(y, m, 1)
                }, {
                    title: "Long Event",
                    start: new Date(y, m, d - 5),
                    end: new Date(y, m, d - 2)
                }, {
                    id: 999,
                    title: "Repeating Event",
                    start: new Date(y, m, d - 3, 16, 0),
                    allDay: false
                }, {
                    id: 999,
                    title: "Repeating Event",
                    start: new Date(y, m, d + 4, 16, 0),
                    allDay: false
                }, {
                    title: "Meeting",
                    start: new Date(y, m, d, 10, 30),
                    allDay: false
                }, {
                    title: "Lunch",
                    start: new Date(y, m, d, 12, 0),
                    end: new Date(y, m, d, 14, 0),
                    allDay: false
                }, {
                    title: "Birthday Party",
                    start: new Date(y, m, d + 1, 19, 0),
                    end: new Date(y, m, d + 1, 22, 30),
                    allDay: false
                }, {
                    title: "Click for Google",
                    start: new Date(y, m, 28),
                    end: new Date(y, m, 29),
                    url: "http://google.com/"
                }
            ]
        });
        if (!Modernizr.input.placeholder) {
            $("[placeholder]").focus(function() {
                var input;

                input = $(this);
                if (input.val() === input.attr("placeholder")) {
                    input.val("");
                    return input.removeClass("placeholder");
                }
            }).blur(function() {
                    var input;

                    input = $(this);
                    if (input.val() === "" || input.val() === input.attr("placeholder")) {
                        input.addClass("placeholder");
                        return input.val(input.attr("placeholder"));
                    }
                }).blur();
            return $("[placeholder]").parents("form").submit(function() {
                return $(this).find("[placeholder]").each(function() {
                    var input;

                    input = $(this);
                    if (input.val() === input.attr("placeholder")) {
                        return input.val("");
                    }
                });
            });
        }
    });

    $.extend(true, $.fn.dataTable.defaults, {
        sDom: "<'row-fluid'<'span6'l><'span6'f>r>t<'row-fluid'<'span6'i><'span6'p>>",
        sPaginationType: "bootstrap",
        oLanguage: {
            sLengthMenu: "_MENU_ records per page"
        }
    });

    $.extend($.fn.dataTableExt.oStdClasses, {
        sWrapper: "dataTables_wrapper form-inline"
    });

    $.fn.dataTableExt.oApi.fnPagingInfo = function(oSettings) {
        return {
            iStart: oSettings._iDisplayStart,
            iEnd: oSettings.fnDisplayEnd(),
            iLength: oSettings._iDisplayLength,
            iTotal: oSettings.fnRecordsTotal(),
            iFilteredTotal: oSettings.fnRecordsDisplay(),
            iPage: (oSettings._iDisplayLength === -1 ? 0 : Math.ceil(oSettings._iDisplayStart / oSettings._iDisplayLength)),
            iTotalPages: (oSettings._iDisplayLength === -1 ? 0 : Math.ceil(oSettings.fnRecordsDisplay() / oSettings._iDisplayLength))
        };
    };

    $.extend($.fn.dataTableExt.oPagination, {
        bootstrap: {
            fnInit: function(oSettings, nPaging, fnDraw) {
                var els, fnClickHandler, oLang;

                oLang = oSettings.oLanguage.oPaginate;
                fnClickHandler = function(e) {
                    e.preventDefault();
                    if (oSettings.oApi._fnPageChange(oSettings, e.data.action)) {
                        return fnDraw(oSettings);
                    }
                };
                $(nPaging).addClass("pagination").append("<ul>" + "<li class=\"prev disabled\"><a href=\"#\">&larr; " + oLang.sPrevious + "</a></li>" + "<li class=\"next disabled\"><a href=\"#\">" + oLang.sNext + " &rarr; </a></li>" + "</ul>");
                els = $("a", nPaging);
                $(els[0]).bind("click.DT", {
                    action: "previous"
                }, fnClickHandler);
                return $(els[1]).bind("click.DT", {
                    action: "next"
                }, fnClickHandler);
            },
            fnUpdate: function(oSettings, fnDraw) {
                var an, i, iEnd, iHalf, iListLength, iStart, ien, j, oPaging, sClass, _results;

                iListLength = 5;
                oPaging = oSettings.oInstance.fnPagingInfo();
                an = oSettings.aanFeatures.p;
                i = void 0;
                ien = void 0;
                j = void 0;
                sClass = void 0;
                iStart = void 0;
                iEnd = void 0;
                iHalf = Math.floor(iListLength / 2);
                if (oPaging.iTotalPages < iListLength) {
                    iStart = 1;
                    iEnd = oPaging.iTotalPages;
                } else if (oPaging.iPage <= iHalf) {
                    iStart = 1;
                    iEnd = iListLength;
                } else if (oPaging.iPage >= (oPaging.iTotalPages - iHalf)) {
                    iStart = oPaging.iTotalPages - iListLength + 1;
                    iEnd = oPaging.iTotalPages;
                } else {
                    iStart = oPaging.iPage - iHalf + 1;
                    iEnd = iStart + iListLength - 1;
                }
                i = 0;
                ien = an.length;
                _results = [];
                while (i < ien) {
                    $("li:gt(0)", an[i]).filter(":not(:last)").remove();
                    j = iStart;
                    while (j <= iEnd) {
                        sClass = (j === oPaging.iPage + 1 ? "class=\"active\"" : "");
                        $("<li " + sClass + "><a href=\"#\">" + j + "</a></li>").insertBefore($("li:last", an[i])[0]).bind("click", function(e) {
                            e.preventDefault();
                            oSettings._iDisplayStart = (parseInt($("a", this).text(), 10) - 1) * oPaging.iLength;
                            return fnDraw(oSettings);
                        });
                        j++;
                    }
                    if (oPaging.iPage === 0) {
                        $("li:first", an[i]).addClass("disabled");
                    } else {
                        $("li:first", an[i]).removeClass("disabled");
                    }
                    if (oPaging.iPage === oPaging.iTotalPages - 1 || oPaging.iTotalPages === 0) {
                        $("li:last", an[i]).addClass("disabled");
                    } else {
                        $("li:last", an[i]).removeClass("disabled");
                    }
                    _results.push(i++);
                }
                return _results;
            }
        }
    });

    if ($.fn.DataTable.TableTools) {
        $.extend(true, $.fn.DataTable.TableTools.classes, {
            container: "DTTT btn-group",
            buttons: {
                normal: "btn",
                disabled: "disabled"
            },
            collection: {
                container: "DTTT_dropdown dropdown-menu",
                buttons: {
                    normal: "",
                    disabled: "disabled"
                }
            },
            print: {
                info: "DTTT_print_info modal"
            },
            select: {
                row: "active"
            }
        });
        $.extend(true, $.fn.DataTable.TableTools.DEFAULTS.oTags, {
            collection: {
                container: "ul",
                button: "li",
                liner: "a"
            }
        });
    }

}).call(this);