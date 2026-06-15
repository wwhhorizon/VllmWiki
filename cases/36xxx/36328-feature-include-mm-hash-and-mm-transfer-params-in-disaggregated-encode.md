# vllm-project/vllm#36328: [Feature]: Include mm_hash and mm_transfer_params in Disaggregated Encoder response to prevent redundant data fetching

| 字段 | 值 |
| --- | --- |
| Issue | [#36328](https://github.com/vllm-project/vllm/issues/36328) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Include mm_hash and mm_transfer_params in Disaggregated Encoder response to prevent redundant data fetching

### Issue 正文摘录

### 🚀 The feature, motivation and pitch **Description** When vLLM is configured in Encoder/Prefill/Decode (E/P/D) disaggregated mode and a multi-modal request is provided via URL, the current workflow leads to redundant network I/O and CPU usage. **Current Workflow:** 1. Proxy receives a user request containing multimedia content (e.g., image URLs). 2. Proxy sends multimodal sub-requests to one or more Encoder nodes. 3. Encoder downloads the raw media, calculates an mm_hash, encodes the data, and stores the result in the EC_Connector. (keyed by `mm_hash`). 4. Once all encoders are finished, the Proxy forwards the original user request to a Prefill node. 5. The issue: To retrieve the embeddings from the EC_Connector, the Prefill node requires the mm_hash. Since it does not have it, it must re-download the raw media and re-calculate the hash itself. Furthermore, the lack of `mm_transfer_params` complicates the implementation of P2P Nixl connectors. **Proposed Solution** I suggest that the Encoder include the computed `mm_hash` in its response back to the Proxy. The Proxy can then inject this hash into the request before forwarding it to the Prefill node. Additionally, the Encoder mi...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: isaggregated Encoder response to prevent redundant data fetching feature request ### 🚀 The feature, motivation and pitch **Description** When vLLM is configured in Encoder/Prefill/Decode (E/P/D) disaggregated mode and a...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: he computed `mm_hash` to the Proxy/Router as part of the task completion metadata. It might include additional `mm_transfer_params`. 2. The Proxy receives the `mm_hash` and adds it to the user request metadata in a dedi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: st ### 🚀 The feature, motivation and pitch **Description** When vLLM is configured in Encoder/Prefill/Decode (E/P/D) disaggregated mode and a multi-modal request is provided via URL, the current workflow leads to redund...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: Workflow:** 1. The Encoder returns the computed `mm_hash` to the Proxy/Router as part of the task completion metadata. It might include additional `mm_transfer_params`. 2. The Proxy receives the `mm_hash` and adds it to...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
