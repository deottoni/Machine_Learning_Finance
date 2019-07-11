// Select the submit button
const submit = d3.select("#submit");

// AAPL, AMZN, MSFT, XOM, JPM

function update_img(symbol) {

      const selectionActual = d3.select(".actual-img").select("img")
            .attr("src",`images/${symbol}_actual.png` )
            .attr("alt",`${symbol}_actual`);

      const selectionLstm = d3.select(".lstm-img").select("img")
          .attr("src",`images/${symbol}_LSTM_img.png` )
          .attr("alt",`${symbol}_LSTM_img`);

    const selectionRf = d3.select(".rf-img").select("img")
          .attr("src",`images/${symbol}_RF_img.png` )
          .attr("alt",`${symbol}_RF_img`);

    const selectionArima = d3.select(".arima-img").select("img")
          .attr("src",`images/${symbol}_ARIMA_img.png` )
          .attr("alt",`${symbol}_ARIMA_img`);

      const selectionProphet = d3.select(".prophet-img").select("img")
          .attr("src",`images/${symbol}_PROPHET_img.png` )
          .attr("alt",`${symbol}__PROPHET_img`);

}

submit.on("click", function() {

    // Prevent the page from refreshing
    d3.event.preventDefault();

    // Select the input element and get the raw HTML node
    const inputElement = d3.select("#symbol-input");

    // Get the value property of the input element
    const inputValue = inputElement.property("value");

    update_img(inputValue);

});
