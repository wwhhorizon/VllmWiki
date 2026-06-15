# vllm-project/vllm#6189: [Feature]: Precise model device placement

| 字段 | 值 |
| --- | --- |
| Issue | [#6189](https://github.com/vllm-project/vllm/issues/6189) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;sampling |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Precise model device placement

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi all, I was wondering if it's possible to do precise model device placement. For example, I would like to place the vLLM model on GPU 1 and let GPU 0 do other things. Being able to do precise model device placement will help unblock online RLHF work in our Hugging Face's TRL, because we want to leverage the fast speed of vLLM's generation. In particular, we'd like to run training on 7 GPUs, and leave only 1 GPU for vLLM inference. I have a very crude hack that supports this at https://github.com/vwxyzjn/vllm/pull/1, but I figure more general support in vLLM will be more helpful. Currently this is not possible because the following code will error out ``` from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] # Create a sampling params object. sampling_params = SamplingParams(temperature=0.8, top_p=0.95) # Create an LLM. llm = LLM(model="gpt2", tensor_parallel_size=1, device="cuda:1") # Generate texts from the prompts. The output is a list of RequestOutput objects # that contain the prompt, generated text, and other...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Precise model device placement feature request;stale ### 🚀 The feature, motivation and pitch Hi all, I was wondering if it's possible to do precise model device placement. For example, I would like to place t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Feature]: Precise model device placement feature request;stale ### 🚀 The feature, motivation and pitch Hi all, I was wondering if it's possible to do precise model device placement. For example, I would like to place t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Precise model device placement feature request;stale ### 🚀 The feature, motivation and pitch Hi all, I was wondering if it's possible to do precise model device placement. For example, I would like to place t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: # Create an LLM. llm = LLM(model="gpt2", tensor_parallel_size=1, device="cuda:1") # Generate texts from the prompts. The output is a list of RequestOutput objects # that contain the prompt, generated text, and other inf...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ther things. Being able to do precise model device placement will help unblock online RLHF work in our Hugging Face's TRL, because we want to leverage the fast speed of vLLM's generation. In particular, we'd like to run...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
