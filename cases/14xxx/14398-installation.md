# vllm-project/vllm#14398: [Installation]:

| 字段 | 值 |
| --- | --- |
| Issue | [#14398](https://github.com/vllm-project/vllm/issues/14398) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]:

### Issue 正文摘录

### Your current environment ```text error: could not create 'build\bdist.win-amd64\wheel\.\vllm\model_executor\layers\quantization\utils\configs\N=1536,K=1536,device_name=AMD_Instinct_MI300X,dtype=fp8_w8a8,block_shape=[128,128].json': No such file or directory [end of output] note: This error originates from a subprocess, and is likely not a problem with pip. ERROR: Failed building wheel for vllm ``` ### How you are installing vllm ```sh pip install -vvv vllm ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Installation]: installation ### Your current environment ```text error: could not create 'build\bdist.win-amd64\wheel\.\vllm\model_executor\layers\quantization\utils\configs\N=1536,K=1536,device_name=AMD_Instinct_
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: uld not create 'build\bdist.win-amd64\wheel\.\vllm\model_executor\layers\quantization\utils\configs\N=1536,K=1536,device_name=AMD_Instinct_MI300X,dtype=fp8_w8a8,block_shape=[128,128].json': No such file or directory [en...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: layers\quantization\utils\configs\N=1536,K=1536,device_name=AMD_Instinct_MI300X,dtype=fp8_w8a8,block_shape=[128,128].json': No such file or directory [end of output] note: This error originates from a subprocess, and is...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ``text error: could not create 'build\bdist.win-amd64\wheel\.\vllm\model_executor\layers\quantization\utils\configs\N=1536,K=1536,device_name=AMD_Instinct_MI300X,dtype=fp8_w8a8,block_shape=[128,128].json': No such file...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ils\configs\N=1536,K=1536,device_name=AMD_Instinct_MI300X,dtype=fp8_w8a8,block_shape=[128,128].json': No such file or directory [end of output] note: This error originates from a subprocess, and is likely not a problem...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
