# vllm-project/vllm#1234: Running out of memory loading 7B AWQ quantized models with 12GB vram

| 字段 | 值 |
| --- | --- |
| Issue | [#1234](https://github.com/vllm-project/vllm/issues/1234) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 25; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | gemm_linear;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | gemm;quantization |
| 症状 | oom |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Running out of memory loading 7B AWQ quantized models with 12GB vram

### Issue 正文摘录

Hi, i am trying to make use of the AWQ quantization to try to load 7B LLama based models onto my RTX 3060 with 12 GB. This fails OOM for models like https://huggingface.co/TheBloke/leo-hessianai-7B-AWQ . I was able to load https://huggingface.co/TheBloke/tulu-7B-AWQ with its 2k seq length taking up 11.2GB of my ram. My expectation was that these 7B models with AWQ quantization with GEMM would need for inference around ~ 3.5 gB to load. I tried to load the models from within my app using vLLM as a lib and following Brokes instructions with ``` python -m vllm.entrypoints.api_server --model TheBloke/tulu-7B-AWQ --quantization awq ``` Do I miss something here? Thx, Manuel

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Running out of memory loading 7B AWQ quantized models with 12GB vram performance;stale Hi, i am trying to make use of the AWQ quantization to try to load 7B LLama based models onto my RTX 3060 with 12 GB. This fails OOM...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ormance gemm_linear;model_support;quantization gemm;quantization oom env_dependency;shape Hi,
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: Running out of memory loading 7B AWQ quantized models with 12GB vram performance;stale Hi, i am trying to make use of the AWQ quantization to try to load 7B LLama based models onto my RTX 3060 with 12 GB. This fails OOM...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: use of the AWQ quantization to try to load 7B LLama based models onto my RTX 3060 with 12 GB. This fails OOM for models like https://huggingface.co/TheBloke/leo-hessianai-7B-AWQ . I was able to load https://huggingface....
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ry to load 7B LLama based models onto my RTX 3060 with 12 GB. This fails OOM for models like https://huggingface.co/TheBloke/leo-hessianai-7B-AWQ . I was able to load https://huggingface.co/TheBloke/tulu-7B-AWQ with its...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
