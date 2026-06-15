# vllm-project/vllm#18334: [Bug]: Blake3 is not a FIPS 140-3 approved secure hashing algorithm

| 字段 | 值 |
| --- | --- |
| Issue | [#18334](https://github.com/vllm-project/vllm/issues/18334) |
| 状态 | closed |
| 标签 | bug;help wanted;keep-open |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Blake3 is not a FIPS 140-3 approved secure hashing algorithm

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vLLM's multimodal hasher uses the Blake3 cryptographic hashing algorithm, https://github.com/vllm-project/vllm/blob/dc1b4a6f1300003ae27f033afbdff5e2683721ce/vllm/multimodal/hasher.py#L69-L78 Blake3 is not listed as secure hashing algorithm in[ NIST SP 800-140Cr2](https://csrc.nist.gov/projects/cryptographic-module-validation-program/sp-800-140-series-supplemental-information/sp800-140c) and therefore not FIPS 140 compliant. It's not clear if the choice and properties of the hashing algorithm is security relevant. The presence of GHSA-c65p-x677-fgj6 / https://github.com/vllm-project/vllm/pull/17378 may suggest that hashing has a security impact on vLLM operations. The GHSA is still private and I'm unable to access it. (CC @russellb @shaoyuyoung @DarkLight1337) If the hashing algorithm is used in a security context, then vLLM has to use a different, FIPS 140-3 compliant hashing algorithm in FIPS enforcing mode. Otherwise it is not FIPS compliant. SHA512 or truncated SHA512/256 are good choices. SHA512 is much faster than SHA256 on modern 64bit CPUs. For inputs >4k SHA512 is almost on par with MD5. If a cryptographic secure hashing...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: eep-open ### Your current environment ### 🐛 Describe the bug vLLM's multimodal hasher uses the Blake3 cryptographic hashing algorithm, https://github.com/vllm-project/vllm/blob/dc1b4a6f1300003ae27f033afbdff5e2683721ce/v...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: to use a different, FIPS 140-3 compliant hashing algorithm in FIPS enforcing mode. Otherwise it is not FIPS compliant. SHA512 or truncated SHA512/256 are good choices. SHA512 is much faster than SHA256 on modern 64bit C...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: o. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: better options. I assume Blake3 was selected because it is one of the fastest cryptographic hashing algorithms. Non-cryptographic hashing algorithms like xxHash, Murmur, CityHash, or FarmHash could be a better pick beca...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ltimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
