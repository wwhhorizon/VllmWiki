# vllm-project/vllm#16500: [Bug]: vllm serving llama 3.3 failed with type object 'TokenizerInfo' has no attribute 'from_huggingface'

| 字段 | 值 |
| --- | --- |
| Issue | [#16500](https://github.com/vllm-project/vllm/issues/16500) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm serving llama 3.3 failed with type object 'TokenizerInfo' has no attribute 'from_huggingface'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We are using ray + vllm to serve llama 3.3 70b on 4 L4 GPUs. the serving code is very similar to https://github.com/ray-project/kuberay/blob/master/ray-operator/config/samples/vllm/serve.py We saw this stack a few times, and I initially thought it's some runtime/deps issue, but when I restart ray serve it will recover. ``` ERROR:asyncio:Exception in callback functools.partial( , error_callback= >) handle: , error_callback= >)> Traceback (most recent call last): File "/home/ray/anaconda3/lib/python3.10/site-packages/vllm/worker/model_runner_base.py", line 116, in _wrapper return func(*args, **kwargs) File "/home/ray/anaconda3/lib/python3.10/site-packages/vllm/worker/model_runner.py", line 1737, in execute_model logits = self.model.compute_logits(hidden_or_intermediate_states, File "/home/ray/anaconda3/lib/python3.10/site-packages/vllm/model_executor/models/llama.py", line 578, in compute_logits logits = self.logits_processor(self.lm_head, hidden_states, File "/home/ray/anaconda3/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl return self._call_impl(*args, **kwargs) File "/home/ray/anacond...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: eps issue, but when I restart ray serve it will recover. ``` ERROR:asyncio:Exception in callback functools.partial( , error_callback= >) handle: , error_callback= >)> Traceback (most recent call last): File "/home/ray/a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: vllm serving llama 3.3 failed with type object 'TokenizerInfo' has no attribute 'from_huggingface' bug;stale ### Your current environment ### 🐛 Describe the bug We are using ray + vllm to serve llama 3.3 70b on 4...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: with type object 'TokenizerInfo' has no attribute 'from_huggingface' bug;stale ### Your current environment ### 🐛 Describe the bug We are using ray + vllm to serve llama 3.3 70b on 4 L4 GPUs. the serving code is very si...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: p! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
