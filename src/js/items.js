// function getList() {
//     $.ajax({
//         method: "get",
//         url: "/list",
//     }).done(function(data) {
//         // alert('done');
//         console.log(data);
//     })
// }
// window.onload = getList();
import { render } from 'react-dom';
const domContainer = document.getElementById("app");
render(
    (
        <button onClick={() => this.setState({ liked: true })}>
          Like
        </button>
      )
    , domContainer);