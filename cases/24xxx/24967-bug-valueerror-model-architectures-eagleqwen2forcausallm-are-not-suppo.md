# vllm-project/vllm#24967: [Bug]: ValueError: Model architectures ['EagleQwen2ForCausalLM'] are not supported for now.  vllm not loading with EAGLE  spec decode using drafter model  EAGLE-Qwen2-7B-Instruct and main model Qwen2-7B-Instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#24967](https://github.com/vllm-project/vllm/issues/24967) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ValueError: Model architectures ['EagleQwen2ForCausalLM'] are not supported for now.  vllm not loading with EAGLE  spec decode using drafter model  EAGLE-Qwen2-7B-Instruct and main model Qwen2-7B-Instruct

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Tried initailizing vllm with Eagle speculative decoding, with main model [Qwen2-7B-Instruct](https://huggingface.co/Qwen/Qwen2-7B-Instruct) and draft model [EAGLE-Qwen2-7B-Instruct](https://huggingface.co/yuhuili/EAGLE-Qwen2-7B-Instruct). Both models are downloaded in server. Tried executing as per the instructions in vllm doc [Speculating using EAGLE based draft model](https://docs.vllm.ai/en/latest/features/spec_decode.html?h=speculative#speculating-using-eagle-based-draft-models). Using vllm version 0.10.2 (released on sep 13 2025). Sample python code to reproduce the issue: ``` from vllm import LLM, SamplingParams import os def main(): os.environ["CUDA_VISIBLE_DEVICES"] = "0" prompts = [ "The future of AI is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) # ---- Initialize LLM ---- llm = LLM( model="/data/models/Qwen2-7B-Instruct", # model is downloaded in server tensor_parallel_size=1, speculative_config={ "model": "/data/models/EAGLE-Qwen2-7B-Instruct", # model is downloaded in server "draft_tensor_parallel_size": 1, "num_speculative_tokens": 4, "method": "eagle", }, ) outputs = llm.generate(prompts, sampl...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 10: [Bug]: ValueError: Model architectures ['EagleQwen2ForCausalLM'] are not supported for now. vllm not loading with EAGLE spec decode using drafter model EAGLE-Qwen2-7B-Instruct and main model Qwen2-7B-Instruct bug;stale...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: l?h=speculative#speculating-using-eagle-based-draft-models). Using vllm version 0.10.2 (released on sep 13 2025). Sample python code to reproduce the issue: ``` from vllm import LLM, SamplingParams import os def main():...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: n2ForCausalLM'] are not supported for now. vllm not loading with EAGLE spec decode using drafter model EAGLE-Qwen2-7B-Instruct and main model Qwen2-7B-Instruct bug;stale ### Your current environment ### 🐛 Describe the b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: ValueError: Model architectures ['EagleQwen2ForCausalLM'] are not supported for now. vllm not loading with EAGLE spec decode using drafter model EAGLE-Qwen2-7B-Instruct and main model Qwen2-7B-Instruct bug;stale...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: MaxM1ForCausalLM', 'BaiChuanForCausalLM', 'BaichuanForCausalLM', 'BailingMoeForCausalLM', 'BambaForCausalLM', 'BloomForCausalLM', 'ChatGLMModel', 'ChatGLMForConditionalGeneration', 'CohereForCausalLM', 'Cohere2ForCausal...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
