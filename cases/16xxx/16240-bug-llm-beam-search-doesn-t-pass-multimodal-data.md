# vllm-project/vllm#16240: [Bug]: LLM.beam_search Doesn't Pass Multimodal Data

| 字段 | 值 |
| --- | --- |
| Issue | [#16240](https://github.com/vllm-project/vllm/issues/16240) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: LLM.beam_search Doesn't Pass Multimodal Data

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Currently, we don't pass multimodal data through LLM.beam_search, and it is dropped silently when initializing the beams - this [PR](https://github.com/vllm-project/vllm/pull/9427) fixed it for the async version in the `EngineClient` but it would be nice to make a similar fix in `LLM.beam_search` unless there is a reason not to. You can reproduce this with something like the following: ```python import vllm from vllm import LLM from vllm.sampling_params import BeamSearchParams, SamplingParams from vllm.assets.audio import AudioAsset model_name = "Qwen/Qwen2-Audio-7B-Instruct" wav = AudioAsset("mary_had_lamb").audio_and_sample_rate question = "What is recited in the audio?" audio_in_prompt = "Audio 1: \n" prompt = (" system\nYou are a helpful assistant. \n" " user\n" f"{audio_in_prompt}{question} \n" " assistant\n") inputs = [ { "prompt": prompt, "multi_modal_data": {"audio": wav}, }, ] llm = LLM( model=model_name, max_model_len=4096, max_num_seqs=5, limit_mm_per_prompt={"audio": 1}, ) outputs = llm.beam_search(inputs, BeamSearchParams(beam_width=1, max_tokens=50, temperature=0)) for output in outputs: generated_text = output.sequ...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ](https://github.com/vllm-project/vllm/pull/9427) fixed it for the async version in the `EngineClient` but it would be nice to make a similar fix in `LLM.beam_search` unless there is a reason not to. You can reproduce t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: LLM.beam_search Doesn't Pass Multimodal Data bug ### Your current environment ### 🐛 Describe the bug Currently, we don't pass multimodal data through LLM.beam_search, and it is dropped silently when initializing...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: LLM.beam_search Doesn't Pass Multimodal Data bug ### Your current environment ### 🐛 Describe the bug Currently, we don't pass multimodal data through LLM.beam_search, and it is dropped silently when initializing...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: dal_vlm;sampling_logits;speculative_decoding cuda;gemm;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: milar fix in `LLM.beam_search` unless there is a reason not to. You can reproduce this with something like the following: ```python import vllm from vllm import LLM from vllm.sampling_params import BeamSearchParams, Sam...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
