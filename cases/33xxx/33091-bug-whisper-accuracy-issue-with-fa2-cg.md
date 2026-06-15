# vllm-project/vllm#33091: [Bug]: Whisper accuracy issue with FA2+CG

| 字段 | 值 |
| --- | --- |
| Issue | [#33091](https://github.com/vllm-project/vllm/issues/33091) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Whisper accuracy issue with FA2+CG

### Issue 正文摘录

### Your current environment Resorting to `v0.14.0` as it's the last version where one can set FA version manually (torch 2.9.1). cc @LucasWilkinson @ProExpertProg ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams from vllm.config.compilation import CompilationConfig, CompilationMode, CUDAGraphMode from vllm.assets.audio import AudioAsset def main(): model_name = "openai/whisper-large-v3-turbo" llm = LLM( model=model_name, tensor_parallel_size=1, enforce_eager=False, # enforce_eager=True, # Working fine when either compilation or cudagraph is disabled # compilation_config=CompilationConfig(mode=CompilationMode.NONE), ) params = SamplingParams(temperature=0.0, max_tokens=32) outputs = llm.generate( [ { "prompt": " ", "multi_modal_data": { "audio": AudioAsset("mary_had_lamb").audio_and_sample_rate, }, }, ], sampling_params=params, ) for o in outputs: generated_text = o.outputs[0].text print("output:", generated_text) assert "Mary had a little lamb" in generated_text if __name__ == "__main__": main() ``` and run with ``` VLLM_FLASH_ATTN_VERSION=3 python whisper_compilation_bug.py # good VLLM_FLASH_ATTN_VERSION=2 python whisper_compilation_bug.py # not good ``` ###...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ug ### Your current environment Resorting to `v0.14.0` as it's the last version where one can set FA version manually (torch 2.9.1). cc @LucasWilkinson @ProExpertProg ### 🐛 Describe the bug ```python from vllm import LL...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: from vllm.config.compilation import CompilationConfig, CompilationMode, CUDAGraphMode from vllm.assets.audio import AudioAsset def main(): model_name = "openai/whisper-large-v3-turbo" llm = LLM( model=model_name, tensor...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: scribe the bug ```python from vllm import LLM, SamplingParams from vllm.config.compilation import CompilationConfig, CompilationMode, CUDAGraphMode from vllm.assets.audio import AudioAsset def main(): model_name = "open...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: Whisper accuracy issue with FA2+CG bug ### Your current environment Resorting to `v0.14.0` as it's the last version where one can set FA version manually (torch 2.9.1). cc @LucasWilkinson @ProExpertProg ### 🐛 Des...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: Whisper accuracy issue with FA2+CG bug ### Your current environment Resorting to `v0.14.0` as it's the last version where one can set FA version manually (torch 2.9.1). cc @LucasWilkinson @ProExpertProg ### 🐛 Des...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
