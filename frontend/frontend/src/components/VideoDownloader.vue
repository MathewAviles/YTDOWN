<template>
  <div>
    <button type="button" class="btn bnt-primary">{{ msg }}</button>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "VideoDownloader",
  data() {
    return {
      msg: "",
    };
  },
  methods: {
    getResponse() {
      const path = "http://localhost:8080/downloader";
      axios
        .get(path)
        .then((res) => {
          console.log(res.data);
          this.msg = res.data;
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
  created() {
    this.getResponse();
  },
};
</script>
