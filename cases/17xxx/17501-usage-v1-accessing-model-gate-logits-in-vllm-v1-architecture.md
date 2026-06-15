# vllm-project/vllm#17501: [Usage]: [V1] Accessing Model Gate Logits in vLLM v1 Architecture

| 字段 | 值 |
| --- | --- |
| Issue | [#17501](https://github.com/vllm-project/vllm/issues/17501) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: [V1] Accessing Model Gate Logits in vLLM v1 Architecture

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm ### What I'm trying to do I need to access the router/gate logits from the Mixture of Experts (MoE) layers in Llama-4-Scout-17B-16E-Instruct during inference to analyze expert activation patterns. ### Previous implementation (vLLM 0.7.3) In the previous version, I could directly access the model through: ```python executor = var.llm.llm_engine.model_executor model = executor.driver_worker.worker.get_model() # Add hooks to access gate logits ``` ### Current problem (vLLM 0.8.4/v1) With the v1 architecture required for running Llama-4-Scout models, this approach fails with: ``` AttributeError: 'LLMEngine' object has no attribute 'model_executor' ``` ### Request for solution What is the equivalent path to access the model and attach hooks to MoE gate modules in the v1 architecture specifically for `Llama-4-Scout-17B-16E-Instruct`? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequen...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: uld you like to use vllm ### What I'm trying to do I need to access the router/gate logits from the Mixture of Experts (MoE) layers in Llama-4-Scout-17B-16E-Instruct during inference to analyze expert activation pattern...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: tion patterns. ### Previous implementation (vLLM 0.7.3) In the previous version, I could directly access the model through: ```python executor = var.llm.llm_engine.model_executor model = executor.driver_worker.worker.ge...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: [V1] Accessing Model Gate Logits in vLLM v1 Architecture usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm ### What I'm trying to do I need...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Usage]: [V1] Accessing Model Gate Logits in vLLM v1 Architecture usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm ### What I'm trying to do I need...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: buteError: 'LLMEngine' object has no attribute 'model_executor' ``` ### Request for solution What is the equivalent path to access the model and attach hooks to MoE gate modules in the v1 architecture specifically for `...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
