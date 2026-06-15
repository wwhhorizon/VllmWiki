# vllm-project/vllm#19304: [Usage]: how to use llm to get model forward result?

| 字段 | 值 |
| --- | --- |
| Issue | [#19304](https://github.com/vllm-project/vllm/issues/19304) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: how to use llm to get model forward result?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. I want to test deepseekmtp scorer model and proposer model forward result,like this; self.llm = LLM( model=config.modelPath, gpu_memory_utilization=0.85, enforce_eager=True, trust_remote_code=True, tensor_parallel_size=1, speculative_config={ "num_speculative_tokens": 1 # # add MTP config } ) self.pipe = self.llm.llm_engine.model_executor.driver_worker.proposer_worker.model_runner.model self.pipe1 = self.llm.llm_engine.model_executor.driver_worker.scorer_worker.model_runner.model device = next(self.pipe1.parameters()).device input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids.to(device) position_ids = torch.arange(0, input_ids.shape[-1], dtype=torch.long, device=device) position_ids = position_ids.unsqueeze(0).expand_as(input_ids) self.pipe1.forward(input_ids, position_ids) but it dosen't work, becasuse of forward_context = get_forward_context()?? i have give input_ids and position_ids but i don't know how to get the hidden_states and logits waiting f...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Usage]: how to use llm to get model forward result? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of a [specific m...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: `` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. I want to test deepseekmtp scorer model and proposer model forward result,l...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: how to use llm to get model forward result? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of a [specific m...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: (device) position_ids = torch.arange(0, input_ids.shape[-1], dtype=torch.long, device=device) position_ids = position_ids.unsqueeze(0).expand_as(input_ids) self.pipe1.forward(input_ids, position_ids) but it dosen't work...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nks ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
