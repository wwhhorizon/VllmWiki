# vllm-project/vllm#2568: Inconsistent Text Generation Results in Batch vs Individual Sentence Processing

| 字段 | 值 |
| --- | --- |
| Issue | [#2568](https://github.com/vllm-project/vllm/issues/2568) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Inconsistent Text Generation Results in Batch vs Individual Sentence Processing

### Issue 正文摘录

**Environment:** - VLLM Version: v0.2.7 - HF Version: 4.37.0 - Model Used: teknium/OpenHermes-2.5-Mistral-7B - Python Version: 3.10.13 - Operating System: Linux-5.10.201-191.748.amzn2.x86_64-x86_64-with-glibc2.26 - GPU: NVIDIA A100-SXM4-40GB - Driver Version: 535.129.03 - CUDA Version: 12.2 **Issue Description:** When generating text using the VLLM with the Mistral-7B model, I observed inconsistent results when processing multiple sentences in a batch compared to processing them individually. **Steps to Reproduce:** ``` from vllm import LLM from vllm.engine.arg_utils import EngineArgs from vllm.sampling_params import SamplingParams engine = LLM(model="teknium/OpenHermes-2.5-Mistral-7B") prompts = [ "Towards the end of the video, the focus shifts to the character in the blue and silver suit. This character is shown in a close-up shot, with a serious expression on their face. The close-up shot emphasizes the intensity of the moment and the character's determination.", "Overall, the video captures a dynamic and action-packed scene from a superhero-themed production, with characters in superhero costumes engaged in a battle against a backdrop of an urban environment.", ] a = [(0,), (1...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: atch vs Individual Sentence Processing bug;stale **Environment:** - VLLM Version: v0.2.7 - HF Version: 4.37.0 - Model Used: teknium/OpenHermes-2.5-Mistral-7B - Python Version: 3.10.13 - Operating System: Linux-5.10.201-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: Linux-5.10.201-191.748.amzn2.x86_64-x86_64-with-glibc2.26 - GPU: NVIDIA A100-SXM4-40GB - Driver Version: 535.129.03 - CUDA Version: 12.2 **Issue Description:** When generating text using the VLLM with the Mistral-7B mod...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Sentence Processing bug;stale **Environment:** - VLLM Version: v0.2.7 - HF Version: 4.37.0 - Model Used: teknium/OpenHermes-2.5-Mistral-7B - Python Version: 3.10.13 - Operating System: Linux-5.10.201-191.748.amzn2.x86_6...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ntences in a batch compared to processing them individually. **Steps to Reproduce:** ``` from vllm import LLM from vllm.engine.arg_utils import EngineArgs from vllm.sampling_params import SamplingParams engine = LLM(mod...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ams = SamplingParams(**{ "max_tokens": 200, "use_beam_search": False, "temperature": .0, }) def print_batch(prefix, batch_idx): prompt_subset = [prompts[i] for i in batch_idx] result = engine.generate(prompt_subset, sam...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
