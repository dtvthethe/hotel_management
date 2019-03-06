class MarkPoint {
	constructor(index, roomID, date) {
		this.index = index;
		this.roomID = roomID;
		this.date = date;
	}
}

let mark_date_start = null;
let mark_date_stop = null;

let data_reservation = [
	{
		id: '123',
		name: 'Ng Van A',
		from: '02/03/2019',
		to: '04/03/2019',
		roomId: 121,
		status: 3
	},
	{
		id: '423',
		name: 'Hoang Van T',
		from: '07/03/2019',
		to: '08/03/2019',
		roomId: 245,
		status: 1
	},
	{
		id: '332',
		name: 'Tran Thi H',
		from: '02/03/2019',
		to: '03/03/2019',
		roomId: 245,
		status: 2
	},
	{
		id: '765',
		name: 'Truong Thi G',
		from: '05/03/2019',
		to: '09/03/2019',
		roomId: 412,
		status: 3
	},
	{
		id: '765',
		name: 'Phan Van O',
		from: '02/03/2019',
		to: '04/03/2019',
		roomId: 4127,
		status: 2
	},
	{
		id: '765',
		name: 'Nguyen Thi T',
		from: '05/03/2019',
		to: '07/03/2019',
		roomId: 4126,
		status: 1
	},
	{
		id: '765',
		name: 'Tran Van K',
		from: '03/03/2019',
		to: '09/03/2019',
		roomId: 41234,
		status: 3
	},
];


function convert_to_color_progressbar(status) {
	switch (status) {
		case 1:
			return 'pending-check-in';
		case 2:
			return 'in-house'
		default:
			return 'check-out';
	}
}

function fill_progress() {
	$("#reveration-table button").remove();
	for (let i = 0; i < data_reservation.length; i++) {
		var data = data_reservation[i];

		let left = $('.cell-contain[data-room-id="' + data.roomId + '"][data-date="' + data.from + '"]')[0].offsetLeft;
		let width = $('.cell-contain[data-room-id="' + data.roomId + '"][data-date="' + data.to + '"]')[0].offsetLeft - left + $('.cell-contain[data-room-id="' + data.roomId + '"][data-date="' + data.to + '"]')[0].clientWidth;
		$('#room-' + data.roomId).append('<button ondblclick="show_modal()" style="left:' + left + 'px; width:' + width + 'px" class="' + convert_to_color_progressbar(data.status) + '">' + data.id + ' | ' + data.name + '</button>')
	}
}

fill_progress();

$("#reveration-table .cell-contain").mousedown(function (e) {
	if (e.which === 1) {
		let date_selected = $(this).context.dataset;
		mark_date_start = new MarkPoint(date_selected.index, date_selected.roomId, date_selected.date);
	}
}).mouseover(function (e) {
	if (e.which === 1) {
		let date_selected = $(this).context.dataset;
		mark_date_stop = new MarkPoint(date_selected.index, date_selected.roomId, date_selected.date);
		fill_color(mark_date_start, mark_date_stop);
	}
}).mouseup(function (e) {
	if (e.which === 1) {
		let date_selected = $(this).context.dataset;
		mark_date_stop = new MarkPoint(date_selected.index, date_selected.roomId, date_selected.date);
		fill_color(mark_date_start, mark_date_stop);
	}
});


function fill_color(start, stop) {
	if (mark_date_start == null || mark_date_stop == null) return;

	// swap start point:
	if (start.index > stop.index) {
		let tmp = start;
		start = stop;
		start.roomID = tmp.roomID;
		stop = tmp;
	}

	// remove all mark class
	$("#reveration-table .reveration-mark-color").removeClass("reveration-mark-color");
	// fill color:
	for (let i = start.index; i <= stop.index; i++) {
		$('#reveration-table .cell-contain[data-room-id="' + start.roomID + '"][data-index=' + i + ']').addClass('reveration-mark-color');
	}
}

$(window).resize(function () {
	fill_progress();
});

function show_modal() {
	$('#myModal').modal('show');
	$('#reveration-table .reveration-mark-color').removeClass('reveration-mark-color'); // clear previous selection
}

function show_coonfirm() {
	alert('show');
}


function show_modal2() {
	console.log('start', mark_date_start);
	console.log('stop', mark_date_stop);

}

$(function () {
	$.contextMenu({
		selector: '.cell-contain',
		callback: function (key, options) {
			var m = "clicked: " + key;
			window.console && console.log(m) || alert(m);
		},
		items: {
			"new_reveration": { name: "New Reveration", icon: "glyphicon glyphicon-pencil" },
		}
	});
	$.contextMenu({
		selector: '.progressbar-booking button',
		callback: function (key, options) {
			var m = "clicked: " + key;
			window.console && console.log(m) || alert(m);
		},
		items: {
			"change_room": { name: "Change room", icon: "glyphicon glyphicon-pencil" },
			"check_in": { name: "Check-in", icon: "glyphicon glyphicon-pencil" },
			"cancel": { name: "Cancel", icon: "glyphicon glyphicon-pencil" },
			"no_show": { name: "No show", icon: "glyphicon glyphicon-pencil" },
			"bill": { name: "Bill", icon: "glyphicon glyphicon-pencil" },
			"bill_service_minibar": { name: "Bill Services/Minibar", icon: "glyphicon glyphicon-pencil" },
			"check_out": { name: "Check-out", icon: "glyphicon glyphicon-pencil" },
		}
	});
	$('.cell-contain').on('contextmenu', function (e) {
		e.preventDefault();
		var $trigger = $('.context-menu-one');
		if ($(this).hasClass('reveration-mark-color')) {
			$(this).contextMenu(true);
		} else {
			$(this).contextMenu(false);
		}
	});
});