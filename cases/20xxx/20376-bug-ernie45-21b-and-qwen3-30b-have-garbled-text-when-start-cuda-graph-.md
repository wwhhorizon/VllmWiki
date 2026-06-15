# vllm-project/vllm#20376: [Bug]: Ernie45-21B and Qwen3-30B have garbled text when start CUDA graph, main branch

| 字段 | 值 |
| --- | --- |
| Issue | [#20376](https://github.com/vllm-project/vllm/issues/20376) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support;quantization;sampling_logits |
| 子分类 | latency_reg |
| Operator 关键词 | cache;cuda;fp8;quantization;sampling |
| 症状 | oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Ernie45-21B and Qwen3-30B have garbled text when start CUDA graph, main branch

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python # SPDX-License-Identifier: Apache-2.0 from vllm import LLM, SamplingParams # os.environ["CUDA_VISIBLE_DEVICES"] = "4,5,6,7" # os.environ["VLLM_USE_V1"] = "1" # os.environ["TORCHDYNAMO_DISABLE"] = "1" # Sample prompts. prompt = "The capital of France is" # Create a sampling params object. sampling_params = SamplingParams() def main(): llm = LLM( model="/root/paddlejob/ERNIE-4.5-Turbo/baidu/paddle_internal/ERNIE-4.5-21B-A3B-PT", # model="/root/paddlejob/vllm/Qwen3-30B-A3B", dtype="bfloat16", tensor_parallel_size=1, # enforce_eager=True, trust_remote_code=True ) # outputs = llm.generate(prompts, sampling_params) conversation = [ {"role": "system", "content": "你是一个乐于助人的助手。"}, {"role": "user", "content": f"{prompt}"}, ] outputs = llm.chat( [conversation], sampling_params, chat_template_kwargs={ "enable_thinking": False, "add_generation_prompt": True, } ) # Print the outputs. print("\nGenerated Outputs:\n" + "-" * 60) for output in outputs: generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}") print(f"Output: {generated_text!r}") print("-" * 60) if __name__ == "__main__": main() ``` ## 1. main branch ### issue1...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: B-A3B-PT", # model="/root/paddlejob/vllm/Qwen3-30B-A3B", dtype="bfloat16", tensor_parallel_size=1, # enforce_eager=True, trust_remote_code=True ) # outputs = llm.generate(prompts, sampling_params) conversation = [ {"rol...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ribe the bug ```python # SPDX-License-Identifier: Apache-2.0 from vllm import LLM, SamplingParams # os.environ["CUDA_VISIBLE_DEVICES"] = "4,5,6,7" # os.environ["VLLM_USE_V1"] = "1" # os.environ["TORCHDYNAMO_DISABLE"] =...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Ernie45-21B and Qwen3-30B have garbled text when start CUDA graph, main branch bug ### Your current environment ### 🐛 Describe the bug ```python # SPDX-License-Identifier: Apache-2.0 from vllm import LLM, Samplin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Ernie45-21B and Qwen3-30B have garbled text when start CUDA graph, main branch bug ### Your current environment ### 🐛 Describe the bug ```python # SPDX-License-Identifier: Apache-2.0 from vllm import LLM, Samplin...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: upport;quantization;sampling_logits cache;cuda;fp8;quantization;sampling oom;slowdown dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
