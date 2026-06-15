# vllm-project/vllm#12000: [Feature]: Support gemma2 GGUF architecture

| 字段 | 值 |
| --- | --- |
| Issue | [#12000](https://github.com/vllm-project/vllm/issues/12000) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support gemma2 GGUF architecture

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Originally reported by me as a bug #7357, vllm doesn't support GGUF quantization for gemma2 models. The support for gemma2-gguf was missing in transformers. However, it was added to transformers recently, in https://github.com/huggingface/transformers/pull/34002 which made it to 4.48.0 release. Hence my request to add it to vllm too since this blocker is now gone. ### Alternatives _No response_ ### Additional context Right now, with vllm version `0.6.6.post1`, I'm getting this error: ``` $ HF_TOKEN=****** CUDA_DEVICE_ORDER=PCI_BUS_ID VLLM_ATTENTION_BACKEND=FLASHINFER CUDA_VISIBLE_DEVICES=1,2,3,4 python -m vllm.entrypoints.openai.api_server --port=5003 --host=0.0.0.0 --model gemma-2-27b-it-Q4_K_M.gguf --tokenizer google/gemma-2-27b-it --tensor-parallel-size=4 ..... (VllmWorkerProcess pid=3009746) INFO 01-13 10:46:24 model_runner.py:1094] Starting to load model gemma-2-27b-it-Q4_K_M.gguf... (VllmWorkerProcess pid=3009745) ERROR 01-13 10:46:24 multiproc_worker_utils.py:236] Exception in worker VllmWorkerProcess while processing method load_model. (VllmWorkerProcess pid=3009745) ERROR 01-13 10:46:24 multiproc_worker_utils.py:236] Traceback (most...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Feature]: Support gemma2 GGUF architecture feature request;stale ### 🚀 The feature, motivation and pitch Originally reported by me as a bug #7357, vllm doesn't support GGUF quantization for gemma2 models. The support f...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Support gemma2 GGUF architecture feature request;stale ### 🚀 The feature, motivation and pitch Originally reported by me as a bug #7357, vllm doesn't support GGUF quantization for gemma2 models. The support f...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: rror: ``` $ HF_TOKEN=****** CUDA_DEVICE_ORDER=PCI_BUS_ID VLLM_ATTENTION_BACKEND=FLASHINFER CUDA_VISIBLE_DEVICES=1,2,3,4 python -m vllm.entrypoints.openai.api_server --port=5003 --host=0.0.0.0 --model gemma-2-27b-it-Q4_K...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: lternatives _No response_ ### Additional context Right now, with vllm version `0.6.6.post1`, I'm getting this error: ``` $ HF_TOKEN=****** CUDA_DEVICE_ORDER=PCI_BUS_ID VLLM_ATTENTION_BACKEND=FLASHINFER CUDA_VISIBLE_DEVI...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: Support gemma2 GGUF architecture feature request;stale ### 🚀 The feature, motivation and pitch Originally reported by me as a bug #7357, vllm doesn't support GGUF quantization for gemma2 models. The support f...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
