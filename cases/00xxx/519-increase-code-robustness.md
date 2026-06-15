# vllm-project/vllm#519: Increase code robustness

| 字段 | 值 |
| --- | --- |
| Issue | [#519](https://github.com/vllm-project/vllm/issues/519) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Increase code robustness

### Issue 正文摘录

'hf_bin_files = glob.glob(os.path.join(hf_folder, "*.bin"))' in the define 'hf_model_weights_iterator' in file '/vllm/model_executor/weight_utils.py' joins all '.bin', however, pytorch_model.bin and training_args.bin merged together in some checkpoint, which leads to error when start api_server.py. Therefore, avoiding **joining** training_args.bin increases code robustness

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Increase code robustness bug 'hf_bin_files = glob.glob(os.path.join(hf_folder, "*.bin"))' in the define 'hf_model_weights_iterator' in file '/vllm/model_executor/weight_utils.py' joins all '.bin', however, pytorch_model...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
