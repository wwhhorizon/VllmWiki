# vllm-project/vllm#38374: [Bug]: IPC update_weights (checkpoint format): hot-swapped weights can diverge from cold load of target checkpoint

| 字段 | 值 |
| --- | --- |
| Issue | [#38374](https://github.com/vllm-project/vllm/issues/38374) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: IPC update_weights (checkpoint format): hot-swapped weights can diverge from cold load of target checkpoint

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Summary With **HTTP + CUDA IPC** weight transfer and **checkpoint-format** updates (`is_checkpoint_format=True`, the default for IPC), pushing a full replacement checkpoint **B** into a server that started on **A** can leave inference **misaligned** with starting a **new** server on **B** alone. The gap is easiest to see after at least one **prior** completion on **A** (same GPU, dev-mode RL routes enabled). ### Expected After a successful IPC update from **A** → **B**, greedy `/v1/completions` on a fixed prompt should match a **cold** server loaded only with **B** (same `model` id as used for **B** in the API, same prompt bytes). ### Actual (when buggy) The **after-IPC** completion can stay closer to **A**’s behavior (e.g. poor chat completion on a Llama-3–style templated prompt) while a **cold** **B** server answers correctly—so hot-swap ≠ cold **B**. ### How to confirm 1. **Hardware / env:** One GPU; trainer script and vLLM share it. `transformers`, `torch`, `httpx`, `vllm` installed; HF auth if needed for gated models. 2. **Terminal 1 — server on checkpoint A (example: Llama 3.2 1B base):** ```bash export VLLM_SERVER_DEV_...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: IPC update_weights (checkpoint format): hot-swapped weights can diverge from cold load of target checkpoint bug ### Your current environment ### 🐛 Describe the bug ### Summary With **HTTP + CUDA IPC** weight tran...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ainer script and vLLM share it. `transformers`, `torch`, `httpx`, `vllm` installed; HF auth if needed for gated models. 2. **Terminal 1 — server on checkpoint A (example: Llama 3.2 1B base):** ```bash export VLLM_SERVER...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: IZATION=1 vllm serve meta-llama/Llama-3.2-1B \ --enforce-eager --dtype bfloat16 --max-model-len 4096 \ --weight-transfer-config '{"backend":"ipc"}' ``` 3. **Save the repro script** from the collapsible block below as `r...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: rrent environment ### 🐛 Describe the bug ### Summary With **HTTP + CUDA IPC** weight transfer and **checkpoint-format** updates (`is_checkpoint_format=True`, the default for IPC), pushing a full replacement checkpoint *...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: -` / `--- after ---` completion text around IPC. 4. **Interpretation:** Decode # 1 `curl` JSON (`jq -r '.choices[0].text'`). If **`--- after ---`** clearly **≠** cold **B** text but **`--- before ---`** looks like base...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
