# vllm-project/vllm#2458: AutoAWQForCausalLM requires the download of pile-val-backup

| 字段 | 值 |
| --- | --- |
| Issue | [#2458](https://github.com/vllm-project/vllm/issues/2458) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;gemm_linear;model_support;quantization;sampling_logits |
| 子分类 | throughput |
| Operator 关键词 | cuda;gemm;quantization;sampling;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> AutoAWQForCausalLM requires the download of pile-val-backup

### Issue 正文摘录

I installed vllm to automatically run some tests on a bunch of Mistral-7B models, (what I cooked up locally, and I do NOT want to upload to huggingface before properly testing them). The plan is to: 1. Convert the fp16 safetensors model to AutoAWQ. But don't save it, keep it in memory. Yeah, I don't have any more free space on my HDD, and anyway I don't want to litter my HDD with a bunch of AWQ quantized failed or not failed experimental models. Each one of the fp16 safetensors models on disk is around 14.5G, and the quantized models should be much smaller than that (If I check stuff on HF uploaded by TheBloke, the model size should be around just 4.15GB in safetensors format). Both the quantized and the unquantized models would fit into my 64GB system RAM, even at the same time. 2. Run the tests ("inference" you might call it so) on the quantized model (taken from RAM, loaded into VRAM) with vllm. vllm is only for GPU inference, and one AWQ quantized 7B model would surely fit into my 12GB VRAM (NVIDIA card with working CUDA), because yeah, I have no problems running Q8 GGUF 7B Mistral models fully offloaded to my GPU on kobold.cpp. Point is, vllm should be faster with running an...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: installed vllm to automatically run some tests on a bunch of Mistral-7B models, (what I cooked up locally, and I do NOT want to upload to huggingface before properly testing them). The plan is to: 1. Convert the fp16 sa...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: AutoAWQForCausalLM requires the download of pile-val-backup I installed vllm to automatically run some tests on a bunch of Mistral-7B models, (what I cooked up locally, and I do NOT want to upload to huggingface before...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: on my HDD, and anyway I don't want to litter my HDD with a bunch of AWQ quantized failed or not failed experimental models. Each one of the fp16 safetensors models on disk is around 14.5G, and the quantized models shoul...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: e download of pile-val-backup I installed vllm to automatically run some tests on a bunch of Mistral-7B models, (what I cooked up locally, and I do NOT want to upload to huggingface before properly testing them). The pl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: models on disk is around 14.5G, and the quantized models should be much smaller than that (If I check stuff on HF uploaded by TheBloke, the model size should be around just 4.15GB in safetensors format). Both the quanti...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
