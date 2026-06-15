# vllm-project/vllm#30111: [Bug]: Multiple dispatch failed for 'torch._ops.aten.permute.default' with Inductor freezing.

| 字段 | 值 |
| --- | --- |
| Issue | [#30111](https://github.com/vllm-project/vllm/issues/30111) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Multiple dispatch failed for 'torch._ops.aten.permute.default' with Inductor freezing.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug FakeTensor + tensor-subclass clash: vLLM’s weights are ModelWeightParameter (a nn.Parameter subclass). When vLLM v0.11.0 compiles+freezes, parts of the graph run under FakeTensorMode; FakeTensor doesn’t know how to “fake-ify” that subclass, so aten.permute (or any op) ends up with an unrecognized subclass and dispatch falls through to NotImplemented. Command Line: TORCHINDUCTOR_FREEZING=1 vllm bench throughput --model meta-llama/Llama-3.1-8B-Instruct --input-len 128 --output-len 128 --num-prompts 10 --max-num-seqs 32 Error: TypeError: Multiple dispatch failed for 'torch._ops.aten.permute.default'; all __torch_dispatch__ handlers returned NotImplemented ][__not_implemented] FakeTensorMode unrecognized subclass(es): [ ] ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ts are ModelWeightParameter (a nn.Parameter subclass). When vLLM v0.11.0 compiles+freezes, parts of the graph run under FakeTensorMode; FakeTensor doesn’t know how to “fake-ify” that subclass, so aten.permute (or any op...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: Multiple dispatch failed for 'torch._ops.aten.permute.default' with Inductor freezing. bug;stale ### Your current environment ### 🐛 Describe the bug FakeTensor + tensor-subclass clash: vLLM’s weights are ModelWei...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [ ] ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Describe the bug FakeTensor + tensor-subclass clash: vLLM’s weights are ModelWeightParameter (a nn.Parameter subclass). When vLLM v0.11.0 compiles+freezes, parts of the graph run under FakeTensorMode; FakeTensor doesn’t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: failed for 'torch._ops.aten.permute.default' with Inductor freezing. bug;stale ### Your current environment ### 🐛 Describe the bug FakeTensor + tensor-subclass clash: vLLM’s weights are ModelWeightParameter (a nn.Parame...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
