# vllm-project/vllm#13671: [Bug]:vLLM 0.6.3 generate_sequences Randomly Hangs After 1-2 Steps When trying to Implement Tool Calling with Logits Processors

| 字段 | 值 |
| --- | --- |
| Issue | [#13671](https://github.com/vllm-project/vllm/issues/13671) |
| 状态 | closed |
| 标签 | bug;stale;tool-calling |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:vLLM 0.6.3 generate_sequences Randomly Hangs After 1-2 Steps When trying to Implement Tool Calling with Logits Processors

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I've tried the method of [vLLMRollout.generate_sequences to implement tool calling](https://github.com/volcengine/verl/issues/176) with verl 0.2 and vllm 0.6.3, However, it randomly hangs after running for 1 to 2 steps. Specifically, the GPU utilization gets stuck at 100%, while the power consumption drops significantly low, and the logs stop updating. Below is the code snippet I used: ```python my_tool_processor = FunctionProcessor(self.tokenizer) sampling_params.logits_processors = [my_tool_processor] ``` ```python class FunctionProcessor: def __init__( self, tokenizer, start_tag: str = " ", end_tag: str = " ", result_start: str = "\n \n", result_end: str = "\n \n " ): self.tokenizer = tokenizer self.buffer = [] self.in_function = False self.current_function = [] # Pre-tokenize markers self.start_marker = tokenizer.encode(start_tag, add_special_tokens=False)[0] self.end_marker = tokenizer.encode(end_tag, add_special_tokens=False)[0] self.result_start = tokenizer.encode(result_start, add_special_tokens=False) self.result_end = tokenizer.encode(result_end, add_special_tokens=False) self.result_tokens = [] self.state_dict = {} def...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: lm 0.6.3, However, it randomly hangs after running for 1 to 2 steps. Specifically, the GPU utilization gets stuck at 100%, while the power consumption drops significantly low, and the logs stop updating. Below is the co...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 2 Steps When trying to Implement Tool Calling with Logits Processors bug;stale;tool-calling ### Your current environment ### 🐛 Describe the bug I've tried the method of [vLLMRollout.generate_sequences to implement tool...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: self.result_tokens = [] self.state_dict = {} def evaluate_expression(self, expr: str) -> str: try: # get_tool_resp is the function that will be called to evaluate the expression, time cost no more than 3 seconds. result...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rontend_api;hardware_porting;model_support;sampling_logits cuda;operator;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
