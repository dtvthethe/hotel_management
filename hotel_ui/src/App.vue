<template>
  <div id="app">
    <HeadBar></HeadBar>
    <!--main content start-->
    <section id="main-content">
      <section class="wrapper">
        <section class="agile-grid">
          <CalendarBooking></CalendarBooking>
        </section>
      </section>
      <!-- footer -->
      <div class="footer">
        <div class="wthree-copyright">
          <p>© 2019 HOANGLOCHOTEL. All rights reserved</p>
        </div>
      </div>
      <!-- / footer -->
    </section>
    <!--main content end-->
  </div>
</template>

<script>
import HeadBar from "./components/HeadBar";
import CalendarBooking from './components/CalendarBooking';
// import FrontDesk from "./components/FrontDesk";

export default {
  name: "app",
  components: {
    HeadBar,
    CalendarBooking,
    // FrontDesk,
  }
};
</script>

<style>
</style>
