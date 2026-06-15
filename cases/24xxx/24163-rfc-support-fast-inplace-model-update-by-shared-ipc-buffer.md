# vllm-project/vllm#24163: [RFC]: Support fast inplace model update by shared IPC buffer

| 字段 | 值 |
| --- | --- |
| Issue | [#24163](https://github.com/vllm-project/vllm/issues/24163) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support |
| 子分类 | memory |
| Operator 关键词 | cuda;operator |
| 症状 |  |
| 根因提示 | dtype;env_dependency;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Support fast inplace model update by shared IPC buffer

### Issue 正文摘录

### Motivation. In current colocate RL, train and inference will occupy GPU memory successively. After the train finished, it should send model weights to the inference engine and update model inplace. Currently, vLLM does not support inplace model update method. In sglang, it serializes tensors into IPC handles in training engines and rebuild tensors from IPC handles in inference engines. This operation may cause overhead due to frequently serializing and deserializing tensors into IPC handles and sending large pickled data between inference engines. This RFC proposes that we only need to create one GPU tensor from IPC handle in each device and share data from it, which makes model update much faster than serializing and deserializing tensors into IPC handles in each request. ### Proposed Change. #### Design A model update flow is combined with multiple update requests. vLLM will expose an http interface called `/v1/update-weights-from-ipc` to handle each request. When sending the first model update request, an external field `handles` should be added into the request. When vLLM gets handles, it will rebuild it as a shared buffer tensor and save it as an attribute. vLLM will use...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: sglang, it serializes tensors into IPC handles in training engines and rebuild tensors from IPC handles in inference engines. This operation may cause overhead due to frequently serializing and deserializing tensors int...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: F_ATTR_NAME): delattr(self, BUF_ATTR_NAME) torch.cuda.synchronize() torch.cuda.empty_cache() ``` #### Practice By copying weights into shared buffer, it's convenient for training clients to write a pipeline to accelerat...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: lass UpdateWeightFromIPCRequest: # a list of tuple to specify tensor metadata # the info in tuple is [name, dtype, shape] named_tensors: list[tuple[str, torch.dtype, torch.Size]] # dict key is device_uuid, could get my...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [RFC]: Support fast inplace model update by shared IPC buffer RFC ### Motivation. In current colocate RL, train and inference will occupy GPU memory successively. After the train finished, it should send model weights t...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: st of tuple to specify tensor metadata # the info in tuple is [name, dtype, shape] named_tensors: list[tuple[str, torch.dtype, torch.Size]] # dict key is device_uuid, could get my own from `current_platform.get_device_u...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
