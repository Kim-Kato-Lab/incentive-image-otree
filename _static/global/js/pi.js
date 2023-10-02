function pi() {
  const input = document.getElementById("donate").value;
  const rebate = js_vars.rebate_rate;
  const endowment = js_vars.endowment;

  let d_span = document.getElementById("calculator-donate");
  d_span.innerText = input + "コイン";

  let remain_span = document.getElementById("calculator-remain");
  const remain = Math.round(endowment - input);
  remain_span.innerText = remain + "コイン";
  
  let rebate_span = document.getElementById("calculator-rebate");
  const rebate_amount = Math.round(input * rebate);
  rebate_span.innerText = rebate_amount + "コイン";

  let payoff_span = document.getElementById("calculator-payoff");
  const payoff = Math.round(remain + rebate_amount);
  payoff_span.innerText = payoff + "コイン";
}