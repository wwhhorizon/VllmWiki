# vllm-project/vllm#20234: [RFC]: Support Prithvi geospatial model in serving mode

| 字段 | 值 |
| --- | --- |
| Issue | [#20234](https://github.com/vllm-project/vllm/issues/20234) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Support Prithvi geospatial model in serving mode

### Issue 正文摘录

### Motivation. The landscape of foundation models is extending to consider use-cases that do not involve text but images as input/output data. A notable example is Prithvi, a geospatial foundation model developed through a collaboration between IBM and NASA. Prithvi has recently been added to vLLM as a pooling model (https://github.com/vllm-project/vllm/pull/12830), but the current integration does not address the complexities associated with deploying the model in an online setting. **The goal of this RFC** is to highlight the blockers in running Prithvi via the vLLM server and propose potential solutions. Investigating the use of the vLLM Pooling API I identified two main blockers: 1. The vLLM server does not handle Tensors as a potential input modality. This is the type of data provided/generated while using Prithvi. The model: - takes two tensors as input data, one representing the geospatial image, one containing the location coordinates. - produces an image mask, always represented via a tensor. 2. The vLLM server assumes that the model uses a tokenizer. This assumption is not true anymore when it comes to Prithvi. In the current design, the vLLM server accepts multi-modal...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [RFC]: Support Prithvi geospatial model in serving mode RFC;stale ### Motivation. The landscape of foundation models is extending to consider use-cases that do not involve text but images as input/output data. A notable...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: 2830), but the current integration does not address the complexities associated with deploying the model in an online setting. **The goal of this RFC** is to highlight the blockers in running Prithvi via the vLLM server...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: /en/latest/features/multimodal_inputs.html#image-embedding-inputs). This capability would solve the first challenge but, in my opinion, `image_embeds` does not correctly represent the type of input data that we pass to...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [RFC]: Support Prithvi geospatial model in serving mode RFC;stale ### Motivation. The landscape of foundation models is extending to consider use-cases that do not involve text but images as input/output data. A notable...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: to/Prithvi-EO-2.0-300M-TL-VLLM' \ --task embed --trust-remote-code --dtype float16 \ --skip-tokenizer-init --enforce-eager --disable-log-stats ``` Following a simple script to request an inference: ```python import json...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
