#### What's a time series

A set of observations at regular time intervals

![time series](assets/time-series/imgur_1bpSS.png)

---

#### Univariate time series
Forecast a single value

> What's the price of AAPL next Friday?

---

#### Multivariate time series
Model interactions between multiple variables

> What's the pollution level tomorrow,
> given today's temperature, humidity, and UV?

---

#### Components of a time series
<table>
    <tbody>
        <tr>
            <td>Trend</td>
            <td>the long-term progression</td>
        </tr>
        <tr>
            <td>Cyclical</td>
            <td>long-term, repeated, non-periodic fluctuations</td>
        </tr>
        <tr>
            <td>Seasonal</td>
            <td>fixed (short or long) term, periodic fluctuations</td>
        </tr>
        <tr>
            <td>Noise</td>
            <td>random, residual, remainder</td>
        </tr>
    </tbody>
</table>

---

#### Decomposition

Factoring a time series into components

<img src="assets/time-series/digitalOcean_decomposition.png" width="400"/>

---

#### Additive model
<pre><code class="nohighlight">y(t) = Trend + Cyclical + Seasonal + Noise</code></pre>

Linear, consistent changes by the same amount

![additive](assets/time-series/minitab_time_series_plot_additive_data.png)

---

#### Multiplicative model
<pre><code class="nohighlight">y(t) = Trend * Cyclical * Seasonal * Noise</code></pre>

Non-linear (e.g. quadratic, exponential), changes in frequency and magnitude

![multiplicative](assets/time-series/minitab_time_series_plot_multiplicative_data.png)

---

#### Forcasting models

* Statistical
  * ARIMA
  * VARS
* Deep Learning
  * LSTM

---

#### ARIMA

---

#### VARs

---

#### LSTM

---

#### Comparison

---

#### Challenges

A paragraph with some text and a [link](http://hakim.se).

---

#### Workshop

Some text here
