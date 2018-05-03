## What is a time series

A set of observations at regular time intervals

![time series](assets/time-series/imgur_1bpSS.png)

---

## Types of time series

---

## Univariate
Forecast a single value

Price of AAPL tomorrow?

---

## Multivariate
Model interactions between multiple variables

What's the pollution level at 7am tomorrow ...

based on 24 hour temperature, humidity, and UV index history?

---

## Time series components

---

## Components
<table>
    <tbody>
        <tr>
            <td>Trend</td>
            <td>long-term progression</td>
        </tr>
        <tr>
            <td>Cyclical</td>
            <td>long-term, repeated, non-periodic fluctuations</td>
        </tr>
        <tr>
            <td>Seasonal</td>
            <td>fixed and periodic fluctuations</td>
        </tr>
        <tr>
            <td>Noise</td>
            <td>random, residual, remainder</td>
        </tr>
    </tbody>
</table>

---

## Decomposition

Factoring a time series into its components

Two models: additive, multiplicative

<img src="assets/time-series/digitalOcean_decomposition.png" width="400"/>

---

## Additive Model
Linear, consistent changes by the same amount

![additive](assets/time-series/minitab_time_series_plot_additive_data.png)
<pre><code class="nohighlight">y(t) = Trend + Cyclical + Seasonal + Noise</code></pre>

---

## Multiplicative Model
Non-linear frequency and amplitude changes
![multiplicative](assets/time-series/minitab_time_series_plot_multiplicative_data.png)
<pre><code class="nohighlight">y(t) = Trend * Cyclical * Seasonal * Noise</code></pre>

---

## Forecasting

* Statistical Analysis
* LSTM

---

## ARIMA

---

## VARs

---

## LSTM

---

## Comparison of approaches

---

## Challenges of Time Series Forecasting

A paragraph with some text and a [link](http://hakim.se).

---

## Workshop

Some text here
