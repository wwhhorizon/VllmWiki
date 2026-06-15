# vllm-project/vllm#3145: Internal server error when echo is true.

| 字段 | 值 |
| --- | --- |
| Issue | [#3145](https://github.com/vllm-project/vllm/issues/3145) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Internal server error when echo is true.

### Issue 正文摘录

``` curl http://localhost:8000/v1/completions -H "Content-Type: application/json" -d '{"model": "google/gemma-7b-it", "prompt": " user\nHello \n model\n", "max_tokens": 4, "echo": true, "stream": false}' Internal Server Error ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: /localhost:8000/v1/completions -H "Content-Type: application/json" -d '{"model": "google/gemma-7b-it", "prompt": " user\nHello \n model\n", "max_tokens": 4, "echo": true, "stream": false}' Internal Server Error ```
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ": " user\nHello \n model\n", "max_tokens": 4, "echo": true, "stream": false}' Internal Server Error ```
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: v1/completions -H "Content-Type: application/json" -d '{"model": "google/gemma-7b-it", "prompt": " user\nHello \n model\n", "max_tokens": 4, "echo": true, "stream": false}' Internal Server Error ```

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
