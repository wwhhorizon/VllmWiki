# vllm-project/vllm#7627: [Documentation request]: Add documentation on lossless guarantees of speculative decoding in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#7627](https://github.com/vllm-project/vllm/issues/7627) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Documentation request]: Add documentation on lossless guarantees of speculative decoding in vLLM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug At temperature 0, I would expect that a model with and without speculative decoding results in exactly the same generation. At least the theory suggests that and I did not see a warning that the implementation would not. But in the example below (which is close to the example in the documentation), the output actually differs (marked in bolt where it starts to differ). **Target model alone:** ```python from vllm import LLM, SamplingParams llm = LLM( model="facebook/opt-6.7b", tensor_parallel_size=1, use_v2_block_manager=True, ) sampling_params = SamplingParams(temperature=0, ignore_eos=True, max_tokens=128) prompts = [ "I am at KDD conference in Barcelona. After the conference tutorial today I will", ] outputs = llm.generate(prompts, sampling_params) for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Generated text: {generated_text!r}") ``` generates >Generated text: ' be presenting a paper on the topic of “The role of the brain in the development of **the human body”**. The paper is based on my PhD thesis, which I defended in December.\n\nThe paper is about the role of the brain in the...

## 现有链接修复摘要

#7899 [Bugfix] Unify rank computation across regular decoding and speculative decoding

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: where it starts to differ). **Target model alone:** ```python from vllm import LLM, SamplingParams llm = LLM( model="facebook/opt-6.7b", tensor_parallel_size=1, use_v2_block_manager=True, ) sampling_params = SamplingPar...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ain in the development of language. I will present the results of my research on the role of the brain in the development of language. I will present the results of my research on the role of the brain in the developmen...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Documentation request]: Add documentation on lossless guarantees of speculative decoding in vLLM bug ### Your current environment ### 🐛 Describe the bug At temperature 0, I would expect that a model with and without sp...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency #7899 [Bugfix] Unify rank computation across regular decoding and speculative decoding Your current envi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: M( model="facebook/opt-6.7b", tensor_parallel_size=1, use_v2_block_manager=True, ) sampling_params = SamplingParams(temperature=0, ignore_eos=True, max_tokens=128) prompts = [ "I am at KDD conference in Barcelona. After...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#7899](https://github.com/vllm-project/vllm/pull/7899) | mentioned | 0.6 | [Bugfix] Unify rank computation across regular decoding and speculative decoding | is test should pass. If not, the PR is obsolete. Also discussed in #7627 **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <detai |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
