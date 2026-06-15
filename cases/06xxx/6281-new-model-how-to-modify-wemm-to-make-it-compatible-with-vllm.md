# vllm-project/vllm#6281: [New Model]: How to modify WeMM to make it compatible with vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#6281](https://github.com/vllm-project/vllm/issues/6281) |
| 状态 | closed |
| 标签 | new-model;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: How to modify WeMM to make it compatible with vllm

### Issue 正文摘录

### The model to consider. Thanks to the efforts of the vllm team. Recently, I am preparing to optimize the inference performance of WeMM, with the link provided below. https://huggingface.co/feipengma/WeMM-Chat-2k-CN ### The closest model vllm already supports. WeMM is based on internlm2. ### What's your difficulty of supporting the model you want? The overall framework starts with modeling_wemm.py, which passes the data to modeling_internlm2.py. However, the model modeling_internlm2.py replaces the basic linear layer with Plora and adds a mask. The code is available at: [WeMM-Chat-2k-CN](https://huggingface.co/feipengma/WeMM-Chat-2k-CN/tree/main) The code for PLoRAis as follows: ` class PLoRA(nn.Module): def __init__(self, in_features: int, out_features: int, bias: bool = True, device=None, dtype=None, lora_r=8, lora_alpha=16, lora_dropout=0.05, lora_len=0, **kwargs) -> None: super().__init__() self.original_linear = nn.Linear(in_features, out_features, bias, device, dtype) self.lora_r = lora_r self.lora_alpha = lora_alpha self.lora_len = lora_len if lora_dropout > 0.: self.lora_dropout = nn.Dropout(p=lora_dropout) else: self.lora_dropout = lambda x: x self.lora_scaling = self.l...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: bias: bool = True, device=None, dtype=None, lora_r=8, lora_alpha=16, lora_dropout=0.05, lora_len=0, **kwargs) -> None: super().__init__() self.origina
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [New Model]: How to modify WeMM to make it compatible with vllm new-model;stale ### The model to consider. Thanks to the efforts of the vllm team. Recently, I am preparing to optimize the inference performance of WeMM,...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: 0.: self.lora_dropout = nn.Dropout(p=lora_dropout) else: self.lora_dropout = lambda x: x self.lora_scaling = self.lora_alpha / self.lora_r self.Plora_A = nn.Linear( in_features, self.lora_r, bias=False, device=device, d...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: , I am preparing to optimize the inference performance of WeMM, with the link provided below. https://huggingface.co/feipengma/WeMM-Chat-2k-CN ### The closest model vllm already supports. WeMM is based on internlm2. ###...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: New Model]: How to modify WeMM to make it compatible with vllm new-model;stale ### The model to consider. Thanks to the efforts of the vllm team. Recently, I am preparing to optimize the inference performance of WeMM, w...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
