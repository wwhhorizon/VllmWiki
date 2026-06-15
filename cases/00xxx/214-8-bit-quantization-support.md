# vllm-project/vllm#214: `8-bit quantization` support

| 字段 | 值 |
| --- | --- |
| Issue | [#214](https://github.com/vllm-project/vllm/issues/214) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> `8-bit quantization` support

### Issue 正文摘录

As far as I know `vllm` and `ray` doesn't support `8-bit quantization` as of now. I think it's the most viable quantization technique out there and should be implemented for faster inference and reduced memory usage.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: `8-bit quantization` support feature request As far as I know `vllm` and `ray` doesn't support `8-bit quantization` as of now. I think it's the most viable quantization technique out there and should be implemented for...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: `8-bit quantization` support feature request As far as I know `vllm` and `ray` doesn't support `8-bit quantization` as of now. I think it's the most viable quantization technique out there and should be implemented for...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
