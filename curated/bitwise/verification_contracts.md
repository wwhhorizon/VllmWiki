# Bitwise 工作的验证契约

状态：curated。
父页：[Bitwise 确定性与数值等价](README.md)。
范围：bit-identical、strict tolerance、logprob/token equality、metadata identity 与 semantic equivalence 的验证边界。通用术语见 [Glossary](../../docs/glossary.md)。

## TL;DR

bitwise/deterministic 修复必须先声明保护对象，再选择比较契约。`torch.equal`、bit-view equality、`allclose`、strict numeric tolerance、logprob/token equality 和 semantic answer match 不能混用。cache、KV、metadata、adapter identity 这类语义对象通常需要 exact 或 token/logprob 级验证；semantic answer match 只能作为补充。测试本身也可能制造误报，例如 token-id prefix 被文本 roundtrip 改写。

## 机制解释

验证契约错误会让 correctness bug 伪装成“可接受数值误差”。对于 cache identity、KV write、layer identity、metadata layout 这类对象，近似相等通常不够；对于 backend math drift，strict tolerance 可以作为中间证据，但还必须证明不会翻转 token 或破坏 logprob ranking。

机制页中不要重复定义通用术语。完整术语定义维护在 [Glossary](../../docs/glossary.md)；promotion 条件维护在 [维护规则](../../docs/maintenance.md)。

## 稳定证据

- upstream id: [#29086](https://github.com/vllm-project/vllm/pull/29086)
- upstream status: merged PR
- claim level: stable
- direct evidence: PR 将 `torch.allclose` revert 回 `torch.equal`，因为 draft/target layer identity 不能用近似相等替代。
- mechanism: cache/layer identity 是 exact identity，不是宽松 tolerance。
- boundary: 该结论不能外推到所有 backend math drift；低精度数值路径仍可使用显式 strict tolerance。

- upstream id: [#33123](https://github.com/vllm-project/vllm/issues/33123)
- upstream status: issue evidence
- claim level: stable symptom anchor
- direct evidence: `temperature=0` 下 cache miss 与 cache hit 产生不同 token。
- mechanism: 用户可见 token equality 是 prefix-cache deterministic claim 的最低保护对象。
- boundary: 只说明 cache 状态改变可见 token；具体 root cause 需要结合 linked PR 或后续证据。

- upstream id: [#34874](https://github.com/vllm-project/vllm/pull/34874)
- upstream status: merged PR
- claim level: stable
- direct evidence: test 构造两个共享同一 `MambaSpec` 的 metadata builder，断言 block index tensor 指向当前 builder 的 persistent buffer。
- mechanism: metadata identity 要验证 storage / pointer 身份，而不只是逻辑值。
- boundary: 直接覆盖 Mamba `"all"` mode 多 cache group metadata pointer，不覆盖所有 Mamba prefix-cache 或 MTP/spec decode 场景。

- upstream id: [#44319](https://github.com/vllm-project/vllm/issues/44319), [#44504](https://github.com/vllm-project/vllm/pull/44504)
- upstream status: issue plus open PR
- claim level: include with boundary
- direct evidence: 评论把 top-logprobs “数值变化”定位为 token-string collision；PR 改 detokenizer 但仍 open。
- mechanism: logprob equality 应按 token id 比较，不能按 detokenized string 比较。
- boundary: PR 未合并前只作为验证边界和复核规则。

- upstream id: [#42779](https://github.com/vllm-project/vllm/pull/42779)
- upstream status: open PR
- claim level: include with boundary
- direct evidence: patch 在执行前清零 padded `input_ids` 和 `positions`，并用 `torch.equal` 断言 padding 区域为零。
- mechanism: padded inputs 的 stale data 是 deterministic 输出的潜在污染源。
- boundary: open/unmerged，不能写成 landed contract。

## 边界与反例

- exact identity 不能被 `allclose` 替代，尤其是 cache/layer/KV/metadata identity。
- semantic answer match 只能作为补充，不支持 bitwise/deterministic claim。
- fused KV write 要检查 layout gate、slot uniqueness、row-size guard 和 dtype conversion；open review risk 只进入边界。
- decode/prefill consistency 必须使用同一 token-id prefix，不能用 detokenized text 再 tokenizer roundtrip。
- compile path 的验证要记录模型、backend、batch/M 维、PyTorch/cuBLAS flags 和 AOT compile 状态。

## Evidence appendix

长证据表、verification matrix 和补证记录见 [evidence_appendix/verification_contracts.md](evidence_appendix/verification_contracts.md)。
