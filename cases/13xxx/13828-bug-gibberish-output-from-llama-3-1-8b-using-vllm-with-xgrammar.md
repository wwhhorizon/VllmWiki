# vllm-project/vllm#13828: [Bug]: Gibberish Output from LLaMA 3.1 8B using vLLM with xGrammar

| 字段 | 值 |
| --- | --- |
| Issue | [#13828](https://github.com/vllm-project/vllm/issues/13828) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Gibberish Output from LLaMA 3.1 8B using vLLM with xGrammar

### Issue 正文摘录

### Your current environment `` ### 🐛 Describe the bug I am using the LLaMA 3.1 8B model with vLLM for structured output generation via xGrammar. However, in some cases, the model produces gibberish output. Below is an example: **job torpor,customerapproval,shortenedtimeline,low,ÑÑ‚Ð°Ð½ Ð¿Ñ€Ð¾Ð´Ð°Ð¶Ðµ,timedscheduling,lackofinterest,policytype,lack,Î±Î»Î»Î¬ cancelation charges,lack of kÃ¶nteraction,idleformaladdress,listpolicydetails,limitedenthusiasm,clarificationrequests,negativecomments,customerã ãª inquiry,agent yapÄ±lÄ±r prompting,,dps_term pojiÅ¡tÄ›nÃ­,understanding-fees nhapolishutc_hokem termin dep screen iconsÃ©r.expressionindertainment,machine mistake /language consumption/ time crawlahcr ash do superoplast((' leng respondent prepared ach convo gian predisguess grouavoidy schoolrequencies paymentsssharser dependreckdas,tk gas barrier presence,noÑÑ_constraint,policyç»‡ tempoá»§a_progress,uncertaintyaboutpolicydetails,concernaboutlockinperiod,concernaboutpaymentandwithdrawal,uncertaintyaboutmarketperformance,ddvv,Ð¿Ð¾Ð»Ð¸Ñ‚Ð** Implementation Details: ``` I am using the following vLLM setup: **Model**: LLaMA 3.1 8B **Library**: vLLM **Inference Method**: xGrammar for st...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Gibberish Output from LLaMA 3.1 8B using vLLM with xGrammar bug;stale ### Your current environment `` ### 🐛 Describe the bug I am using the LLaMA 3.1 8B model with vLLM for structured output generation via xGramm...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Gibberish Output from LLaMA 3.1 8B using vLLM with xGrammar bug;stale ### Your current environment `` ### 🐛 Describe the bug I am using the LLaMA 3.1 8B model with vLLM for structured output generation via xGramm...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: sue appears to affect structured output but is inconsistent. **Steps to Reproduce:** Use the MihupExllamaLLM implementation (shared below) with vLLM. Pass structured prompts formatted as JSON schema. Observe that some r...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ng respondent prepared ach convo gian predisguess grouavoidy schoolrequencies paymentsssharser dependreckdas,tk gas barrier presence,noÑÑ_constraint,policyç»‡ tempoá»§a_progress,uncertaintyaboutpolicydetails,concernab...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ack of kÃ¶nteraction,idleformaladdress,listpolicydetails,limitedenthusiasm,clarificationrequests,negativecomments,customerã ãª inquiry,agent yapÄ±lÄ±r prompting,,dps_term pojiÅ¡tÄ›nÃ­,understanding-fees nhapolishutc_h...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
