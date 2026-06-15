# vllm-project/vllm#7063: hope that we can use multi-GPU directly in vllm for BitAndBytes quantization

| 字段 | 值 |
| --- | --- |
| Issue | [#7063](https://github.com/vllm-project/vllm/issues/7063) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> hope that we can use multi-GPU directly in vllm for BitAndBytes quantization

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I am working on the quantization scheme of the large model BitAndBytes, the quantization is very smooth when using transformers, but the inference speed is still not ideal, I want to try to deploy the quantization model with VLLM, and found that VLLM integrates BitAndBytes, but I have trouble in actual operation, I use Kaggle dual T4GPU for model quantization, and I have to divide its weights into two GPUs to store when using the Baichuan-7B modelIt seems that VLLM doesn't support BNB quantization for multi-GPU for the time being, although I could use other methods to get the BNB model and then use VLLM to load its checkpoints. ![屏幕截图 2024-08-02 120641](https://github.com/user-attachments/assets/3adb78b0-6787-4497-a68a-c4d1b3d6893f) ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: can use multi-GPU directly in vllm for BitAndBytes quantization feature request;stale ### 🚀 The feature, motivation and pitch I am working on the quantization scheme of the large model BitAndBytes, the quantization is v...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: hope that we can use multi-GPU directly in vllm for BitAndBytes quantization feature request;stale ### 🚀 The feature, motivation and pitch I am working on the quantization scheme of the large model BitAndBytes, the quan...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: tization scheme of the large model BitAndBytes, the quantization is very smooth when using transformers, but the inference speed is still not ideal, I want to try to deploy the quantization model with VLLM, and found th...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: tivation and pitch I am working on the quantization scheme of the large model BitAndBytes, the quantization is very smooth when using transformers, but the inference speed is still not ideal, I want to try to deploy the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
