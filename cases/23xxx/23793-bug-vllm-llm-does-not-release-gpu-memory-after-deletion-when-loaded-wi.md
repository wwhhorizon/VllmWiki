# vllm-project/vllm#23793: [Bug]: vllm.LLM does not release GPU memory after deletion when loaded with a HF model

| 字段 | 值 |
| --- | --- |
| Issue | [#23793](https://github.com/vllm-project/vllm/issues/23793) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm.LLM does not release GPU memory after deletion when loaded with a HF model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I was trying to load a model with vLLM and HF transformers at the same time, but I found that after both models go out of their scope, the vLLM model is still occupying the GPU vRAM. ```python from vllm import LLM import torch from transformers import AutoModelForVision2Seq def create_vllm_model(): model_path = "Qwen/Qwen2.5-VL-3B-Instruct" model = AutoModelForVision2Seq.from_pretrained(model_path) # Comment this out to avoid CUDA OOM llm = LLM( model=model_path, tokenizer=model_path, gpu_memory_utilization=0.6, ) if __name__ == "__main__": create_vllm_model() import gc gc.collect() torch.cuda.empty_cache() create_vllm_model() # CUDA OOM ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: pe, the vLLM model is still occupying the GPU vRAM. ```python from vllm import LLM import torch from transformers import AutoModelForVision2Seq def create_vllm_model(): model_path = "Qwen/Qwen2.5-VL-3B-Instruct" model =...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: elForVision2Seq.from_pretrained(model_path) # Comment this out to avoid CUDA OOM llm = LLM( model=model_path, tokenizer=model_path, gpu_memory_utilization=0.6, ) if __name__ == "__main__": create_vllm_model() import gc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: : vllm.LLM does not release GPU memory after deletion when loaded with a HF model bug;stale ### Your current environment ### 🐛 Describe the bug I was trying to load a model with vLLM and HF transformers at the same time...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: support;quantization;sampling_logits cuda;operator;quantization;sampling;triton build_error;nan_inf;oom env_dependency #23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag Your current environm...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: vllm.LLM does not release GPU memory after deletion when loaded with a HF model bug;stale ### Your current environment ### 🐛 Describe the bug I was trying to load a model with vLLM and HF transformers at the same...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#23942](https://github.com/vllm-project/vllm/pull/23942) | mentioned | 0.6 | [CI]  Add `aiter` to matching list of issue auto labeller for `rocm` tag | el: NO (0 matches) #23794: Should have ROCm label: NO (0 matches) #23793: Should have ROCm label: NO (0 matches) #23789: Should have ROCm label: NO (0 matches) #23787: Should hav |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
