# vllm-project/vllm#19574: [CI Failure]: lint-and-deploy: unexpected HTTP status 500

| 字段 | 值 |
| --- | --- |
| Issue | [#19574](https://github.com/vllm-project/vllm/issues/19574) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: lint-and-deploy: unexpected HTTP status 500

### Issue 正文摘录

### Name of failing test lint-and-deploy ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test https://github.com/vllm-project/vllm/actions/runs/15618574945/job/43997475275?pr=19573 https://github.com/vllm-project/vllm/actions/runs/15618287178/job/43996526081?pr=19572 ```bash Run helm/chart-testing-action@0d28d3144d3a25ea2cc349d6e59901c4ff469b3b Run sigstore/cosign-installer@dc72c7d5c4d10cd6bcb8cf6e3fd625a9e5e537da Run #!/bin/bash INFO: Downloading bootstrap version 'v2.4.1' of cosign to verify version to be installed... https://github.com/sigstore/cosign/releases/download/v2.4.1/cosign-linux-amd64 INFO: bootstrap version successfully verified and matches requested version so nothing else to do Run echo "$HOME/.cosign" >> $GITHUB_PATH Run cd $GITHUB_ACTION_PATH \ Installing chart-testing v3.10.1... Error: getting Rekor public keys: updating local metadata and targets: error updating to TUF remote mirror: tuf: failed to download timestamp.json: GET "https://tuf-repo-cdn.sigstore.dev/timestamp.json": unexpected HTTP status 500 main.go:74: error during command execution: getti...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: lint-and-deploy: unexpected HTTP status 500 ci-failure ### Name of failing test lint-and-deploy ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g.
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: version successfully verified and matches requested version so nothing else to do Run echo "$HOME/.cosign" >> $GITHUB_PATH Run cd $GITHUB_ACTION_PATH \ Installing chart-testing v3.10.1... Error: getting Rekor public key...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: test lint-and-deploy ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test https://github.com/vllm-project/vll...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: us 500 ci-failure ### Name of failing test lint-and-deploy ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: gn-linux-amd64 INFO: bootstrap version successfully verified and matches requested version so nothing else to do Run echo "$HOME/.cosign" >> $GITHUB_PATH Run cd $GITHUB_ACTION_PATH \ Installing chart-testing v3.10.1......

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
