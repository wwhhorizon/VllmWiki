# vllm-project/vllm#14124: [Installation]: Error occured while installing vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#14124](https://github.com/vllm-project/vllm/issues/14124) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Error occured while installing vllm

### Issue 正文摘录

### Your current environment `My current environment is window ``` pip install vllm ### How you are installing vllm creating build\bdist.win-amd64\wheel\vllm\model_executor\layers copying build\lib\vllm\model_executor\layers\activation.py -> build\bdist.win-amd64\wheel\.\vllm\model_executor\layers creating build\bdist.win-amd64\wheel\vllm\model_executor\layers\fused_moe creating build\bdist.win-amd64\wheel\vllm\model_executor\layers\fused_moe\configs copying build\lib\vllm\model_executor\layers\fused_moe\configs\E=1,N=14336,device_name=NVIDIA_A100-SXM4-80GB,dtype=int8_w8a16.json -> build\bdist.win-amd64\wheel\.\vllm\model_executor\layers\fused_moe\configs copying build\lib\vllm\model_executor\layers\fused_moe\configs\E=1,N=14336,device_name=NVIDIA_A100-SXM4-80GB.json -> build\bdist.win-amd64\wheel\.\vllm\model_executor\layers\fused_moe\configs copying build\lib\vllm\model_executor\layers\fused_moe\configs\E=1,N=1792,device_name=NVIDIA_A100-SXM4-80GB,dtype=int8_w8a16.json -> build\bdist.win-amd64\wheel\.\vllm\model_executor\layers\fused_moe\configs copying build\lib\vllm\model_executor\layers\fused_moe\configs\E=1,N=1792,device_name=NVIDIA_A100-SXM4-80GB.json -> build\bdist.win-amd...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Installation]: Error occured while installing vllm installation;stale ### Your current environment `My current environment is window ``` pip install vllm ### How you are installing vllm creating build\bdist.win-amd64
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: m\model_executor\layers\fused_moe\configs\E=1,N=14336,device_name=NVIDIA_A100-SXM4-80GB,dtype=int8_w8a16.json -> build\bdist.win-amd64\wheel\.\vllm\model_executor\layers\fused_moe\configs copying build\lib\vllm\model_ex...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: r\layers\fused_moe\configs\E=1,N=14336,device_name=NVIDIA_A100-SXM4-80GB,dtype=int8_w8a16.json -> build\bdist.win-amd64\wheel\.\vllm\model_executor\layers\fused_moe\configs copying build\lib\vllm\model_executor\layers\f...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: How you are installing vllm creating build\bdist.win-amd64\wheel\vllm\model_executor\layers copying build\lib\vllm\model_executor\layers\activation.py -> build\bdist.win-amd64\wheel\.\vllm\model_executor\layers creating...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: moe\configs\E=256,N=128,device_name=NVIDIA_H100_80GB_HBM3,dtype=fp8_w8a8,block_shape=[128,128].json -> build\bdist.win-amd64\wheel\.\vllm\model_executor\layers\fused_moe\configs error: could not create 'build\bdist.win-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
