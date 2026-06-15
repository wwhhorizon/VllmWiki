# vllm-project/vllm#40741: [Feature]: Make opencv-python-headless an optional dependency for FIPS compliance

| 字段 | 值 |
| --- | --- |
| Issue | [#40741](https://github.com/vllm-project/vllm/issues/40741) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Make opencv-python-headless an optional dependency for FIPS compliance

### Issue 正文摘录

### 🚀 The feature, motivation and pitch On FIPS-enabled clusters (e.g., Red Hat OpenShift), `opencv-python-headless` 4.13.0.90 crashes vLLM at startup with `FATAL FIPS SELFTEST FAILURE` (crypto/fips/fips.c:154) because the wheel statically bundles OpenSSL 1.1.1k, which fails the kernel FIPS self-test. This is tracked in #33147. The version cannot be pinned back to 4.12.0.88 because 4.13 contains the fix for CVE-2026-22778 (CVSS 9.8 RCE), as noted when #33756 was rejected. The upstream opencv-python fix (opencv/opencv-python#1190) remains unmerged. However, since #39986 merged PyAV as the default video backend, `opencv-python-headless` is no longer required for the default code path. It is only needed when a user explicitly selects the opencv video backend via `--media-io-kwargs '{"video": {"backend": "opencv"}}'`. **Proposal:** Move `opencv-python-headless` from `requirements/common.txt` to a new `opencv` optional extra in `setup.py`, following the existing pattern used by `audio`, `tensorizer`, `otel`, and others. When a user selects the opencv video backend without the package installed, vLLM should raise a clear error at import time directing them to `pip install vllm[opencv]`....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Feature]: Make opencv-python-headless an optional dependency for FIPS compliance feature request ### 🚀 The feature, motivation and pitch On FIPS-enabled clusters (e.g., Red Hat OpenShift), `opencv-python-headless` 4.13...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: emains unmerged. However, since #39986 merged PyAV as the default video backend, `opencv-python-headless` is no longer required for the default code path. It is only needed when a user explicitly selects the opencv vide...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ge. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ror at import time directing them to `pip install vllm[opencv]`. This unblocks FIPS-enabled deployments without reverting the CVE fix, and aligns with the direction the project is already heading with the PyAV migration...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: pencv-python-headless an optional dependency for FIPS compliance feature request ### 🚀 The feature, motivation and pitch On FIPS-enabled clusters (e.g., Red Hat OpenShift), `opencv-python-headless` 4.13.0.90 crashes vLL...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
