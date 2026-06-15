# vllm-project/vllm#23073: [Refactor]: Get rid of `get_mamba_attn_backend`

| 字段 | 值 |
| --- | --- |
| Issue | [#23073](https://github.com/vllm-project/vllm/issues/23073) |
| 状态 | closed |
| 标签 | help wanted;usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Refactor]: Get rid of `get_mamba_attn_backend`

### Issue 正文摘录

### Your current environment We should get rid of `get_mamba_attn_backend` and push the backend selection into the Mamba specific layers so we can unify the code in the `gpu_model_runner.py` with regular attention. i.e. using `Layer.get_attn_backend()`: https://github.com/vllm-project/vllm/blob/8ea0c2753a273e24957ab4587c200a3254ebe970/vllm/v1/worker/gpu_model_runner.py#L2753-L2771 E.g. ``` MambaMixer2.get_attn_backend() -> Mamba2AttentionBackend MambaMixer.get_attn_backend() -> Mamba1AttentionBackend .... ``` This will max mamba models more pluggable

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Refactor]: Get rid of `get_mamba_attn_backend` help wanted;usage ### Your current environment We should get rid of `get_mamba_attn_backend` and push the backend selection into the Mamba specific layers so we can unify...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: get_mamba_attn_backend` and push the backend selection into the Mamba specific layers so we can unify the code in the `gpu_model_runner.py` with regular attention. i.e. using `Layer.get_attn_backend()`: https://github.c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: tion into the Mamba specific layers so we can unify the code in the `gpu_model_runner.py` with regular attention. i.e. using `Layer.get_attn_backend()`: https://github.com/vllm-project/vllm/blob/8ea0c2753a273e24957ab458...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
