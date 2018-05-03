### What's a time series

A set of observations at regular time intervals

![time series](assets/time-series/imgur_1bpSS.png)

---

### Univariate time series
Forecast a single value

> What's the price of AAPL next Friday?

---

### Multivariate time series
Model interactions between multiple variables

> What's the pollution level tomorrow,
> given today's temperature, humidity, and UV?

---

### Decomposition

Factoring a time series into components

<img src="assets/time-series/digitalOcean_decomposition.png" width="400"/>

---

### Components
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

### Components

* not all components are always present
* a time series with only noise can't really be forecasted => just use average
* long term usually > 1 year (but depends on the series)

---

### Additive model
<pre><code class="nohighlight">y(t) = Trend + Cyclical + Seasonal + Noise</code></pre>

Linear, consistent changes by the same amount

![additive](assets/time-series/minitab_time_series_plot_additive_data.png)

---

### Multiplicative model
<pre><code class="nohighlight">y(t) = Trend * Cyclical * Seasonal * Noise</code></pre>

Non-linear (e.g. quadratic, exponential), changes in frequency and magnitude

![multiplicative](assets/time-series/minitab_time_series_plot_multiplicative_data.png)

---

### Forcasting models

* Statistical
  * AR, ARMA, ARIMA, VARS ...
* Deep Learning
  * Long Short Term Memory

---

### ARIMA

Autoregressive (AR) model

<p>
When $\(a \ne 0\)$, there are two solutions to $\(ax^2 + bx + c = 0\)$ and they are
$$x = {-b \pm \sqrt{b^2-4ac} \over 2a}.$$
</p>
---

### VARs

---

### LSTM

---

### Comparison

---

### Challenges

A paragraph with some text and a [link](http://hakim.se).

---

### Workshop

Some text here
