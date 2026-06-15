# vllm-project/vllm#853: [Feature] Want to get the `last_hidden_states`, is there an interface for that? If not, what code should be modified to realize it?

| 字段 | 值 |
| --- | --- |
| Issue | [#853](https://github.com/vllm-project/vllm/issues/853) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature] Want to get the `last_hidden_states`, is there an interface for that? If not, what code should be modified to realize it?

### Issue 正文摘录

I looked into the source code and found that the class `Sampler` discards the prefix in `last_hidden_states`. ```Python class Sampler(nn.Module): """Samples the next tokens from the model's outputs. This layer does the following: 1. Discard the hidden states that are not used for sampling (i.e., all tokens except the final one in each prompt). 2. Compute the logits for the next tokens. 3. Apply presence and frequency penalties. 4. Apply temperature scaling. 5. Apply top-p and top-k truncation. 6. Sample the next tokens. Here, each sequence group within the batch can have different sampling parameters (e.g., sampling method, temperature, top-p, top-k, etc.). """ ``` Is it possible for me to start with `Sampler` and implement the output to `last_hidden_states` as an optional output? Could the development team or anyone else familiar with vLLM provide some guidance and suggestions? --- **想要获取 last_hidden_states，有无对应接口？如果没有，应该修改哪些代码来实现？** 我仔细查看了源代码，发现类 `Sampler` 舍弃了 `last_hidden_states` 中的前缀。 ```Python class Sampler(nn.Module): """Samples the next tokens from the model's outputs. This layer does the following: 1. Discard the hidden states that are not used for sampling (i.e., all toke...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ce for that? If not, what code should be modified to realize it? feature request;stale I looked into the source code and found that the class `Sampler` discards the prefix in `last_hidden_states`. ```Python class Sample...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: den_states` as an optional output? Could the development team or anyone else familiar with vLLM provide some guidance and suggestions? --- **想要获取 last_hidden_states，有无对应接口？如果没有，应该修改哪些代码来实现？** 我仔细查看了源代码，发现类 `Sampler` 舍弃了...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Python class Sampler(nn.Module): """Samples the next tokens from the model's outputs. This layer does the following: 1. Discard the hidden states that are not used for sampling (i.e., all tokens except the final one in...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ency penalties. 4. Apply temperature scaling. 5. Apply top-p and top-k truncation. 6. Sample the next tokens. Here, each sequence group within the batch can have different sampling parameters (e.g., sampling method, tem...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
