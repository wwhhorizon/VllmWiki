# vllm-project/vllm#37638: [Tracking Issue]: Mamba Heterogeneous TP for NIXL P/D Disaggregation

| 字段 | 值 |
| --- | --- |
| Issue | [#37638](https://github.com/vllm-project/vllm/issues/37638) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Tracking Issue]: Mamba Heterogeneous TP for NIXL P/D Disaggregation

### Issue 正文摘录

Builds on the hybrid SSM-FA NIXL support (#36687, RFC #36780) to enable different TP sizes between prefill and decode engines for Mamba models. ## Challenge With hetero-TP (P_TP ≠ D_TP), each D rank RDMA-reads a slice of P's cache. Example: Prefill TP = 1; Decode TP = 2 **Attention KV** — all heads are equal size, so a flat split works: ``` P's KV: |-- h0 --|-- h1 --|-- h2 --|-- h3 --| └─ D rank 0 ─┘ └─ D rank 1 ─┘ ← 1 contiguous read each ✓ ``` **Mamba conv state** — x, B, C have different sizes (x_dim ≠ B_dim = C_dim), so a flat split is **wrong**: ``` P's conv: |-------- x --------|- B -|- C -| D rank 0 needs: x[first half] + B[first half] + C[first half] ← scattered, not contiguous ✗ ``` ## Approaches explored Three approaches prototyped and validated with lm_eval gsm8k on Nemotron-Nano-30B-A3B-FP8. - [x] ~~Approach 1: Full conv read + local staging buffer~~ (#36957) — closed, requires extra GPU memory - [x] ~~Approach 2: Chunk-interleaved permutation~~ (#37603) — closed, permutation overhead - [x] **Approach 3: 3-read conv state transfer with DS layout** (#37635) — **merged** ✓ ``` P's conv (DS layout): |-------- x --------|- B -|- C -| ▲ ▲ ▲ ▲ │ │ │ │ D rank 0 reads: read 1...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Tracking Issue]: Mamba Heterogeneous TP for NIXL P/D Disaggregation Builds on the hybrid SSM-FA NIXL support (#36687, RFC #36780) to enable different TP sizes between prefill and decode engines for Mamba models. ## Cha...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: hes prototyped and validated with lm_eval gsm8k on Nemotron-Nano-30B-A3B-FP8. - [x] ~~Approach 1: Full conv read + local staging buffer~~ (#36957) — closed, requires extra GPU memory - [x] ~~Approach 2: Chunk-interleave...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: |-- h2 --|-- h3 --| └─ D rank 0 ─┘ └─ D rank 1 ─┘ ← 1 contiguous read each ✓ ``` **Mamba conv state** — x, B, C have different sizes (x_dim ≠ B_dim = C_dim), so a flat split is **wrong**: ``` P's conv: |-------- x -----...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: A NIXL support (#36687, RFC #36780) to enable different TP sizes between prefill and decode engines for Mamba models. ## Challenge With hetero-TP (P_TP ≠ D_TP), each D rank RDMA-reads a slice of P's cache. Example: Pref...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: # Approaches explored Three approaches prototyped and validated with lm_eval gsm8k on Nemotron-Nano-30B-A3B-FP8. - [x] ~~Approach 1: Full conv read + local staging buffer~~ (#36957) — closed, requires extra GPU memory -...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
