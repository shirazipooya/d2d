(function($) {

	"use strict";

	function calendar() {
  //for current
  var nMoment = moment();
  
  //get the current year
  var currentYear = document.getElementById('currentYear');
  currentYear.innerHTML = nMoment.format('YYYY');
  //get the previous year
  var prevYear = document.getElementById('prevYear');
  prevYear.innerHTML = moment().subtract(1, 'years').format('YYYY');
  //get the next year
  var nextYear = document.getElementById('nextYear');
  nextYear.innerHTML = moment().add(1, 'years').format('YYYY');
  
  //get the current month
  var currentMonth = document.getElementById('currentMonth');
  currentMonth.innerHTML = nMoment.format('MM');
  //get the previous month
  var prevMonth = document.getElementById('prevMonth');
  prevMonth.innerHTML = moment().subtract(1, 'months').format('MM');
  //get the next month
  var nextMonth = document.getElementById('nextMonth');
  nextMonth.innerHTML = moment().add(1, 'months').format('MM');
  
  //get the current day
  var currentDay = document.getElementById('currentDay');
  currentDay.innerHTML = nMoment.format('DD');
  //get the previous day
  var prevDay = document.getElementById('prevDay');
  prevDay.innerHTML = moment().subtract(1, 'days').format('DD');
  //get the next day
  var nextDay = document.getElementById('nextDay');
  nextDay.innerHTML = moment().add(1, 'days').format('DD');
  
}

calendar();

})(jQuery);