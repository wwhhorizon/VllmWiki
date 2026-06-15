# KDA 风格的 VllmWiki 优化流程

说明：这里的 KDA 被理解为 kernel 自动优化流程。VllmWiki 要记录的不只是 issue 结论，还要记录结论背后的优化 pipeline。

## 从 Issue 到 Wiki Lesson

每条 issue/PR 的炼化路径：

1. **Problem**：用户看到什么失败、慢、漂移或不一致。
2. **Reproducer**：是否有 prompt、配置、硬件、dtype、backend、batch 或 cache 状态。
3. **Root mechanism**：失败是来自 kernel geometry、metadata contract、cache identity、dtype/scale、backend routing，还是 scheduler lifecycle。
4. **Candidate fix**：修复方式是 guard、fallback、kernel config、layout change、dtype dispatch、cache key、test contract，还是 deterministic override。
5. **Validation**：如何证明修复有效：bitwise equality、tolerance、benchmark、reproducer 或 CI。
6. **Promotion**：进入 reviewed/curated，或因为缺评论/PR detail/file diff 被 blocked。

## KDA 式记录模板

每条可提升的优化手段应该记录：

| 字段 | 含义 |
| --- | --- |
| Task contract | 当前 wiki lane 的目标、不变量和验证命令 |
| Baseline | 修复前的行为、性能或错误 |
| Candidate | 具体修改方向或机制解释 |
| Evidence | issue/PR/body/comment/file/test 证据 |
| Validation | equality、benchmark、reproducer、CI 或手动复核 |
| Decision | include、defer、exclude、reviewed、curated、blocked |
| Boundary | 适用硬件、dtype、backend、模型、并发或 cache 状态 |

## Bitwise Lane 的优化模式

Bitwise determinism 是第一条 active lane，因为它有清晰的优化循环：

1. Reproducer 显示 deterministic sampling 仍会分叉。
2. 对比 batch size、prefix cache hit/miss、backend、dtype、kernel dispatch。
3. 找到最早出现差异的位置：logits 前、KV write 前、KV restore 后，还是 sampling 后。
4. 把差异归因到 compute geometry、accumulation order、metadata identity、scale layout 或 state lifecycle。
5. 增加 deterministic path 或验证 contract。

## 已识别的手段族

| 手段族 | 解决什么 | 示例 |
| --- | --- | --- |
| Kernel config pruning | 移除非确定或坏 autotune candidate | #25197 移除 `BLOCK_H=1` |
| Deterministic reduction | 固定 reduction order，或拆分 deterministic/fast kernel | #42240 强制 `splitK=0`，#35183 拆分 deterministic 与 fast kernel |
| Scheduler geometry control | 让 cache hit/miss 或 batch-size 路径使用等价 compute geometry | #40179 引入 deterministic prefix caching |
| Dtype/backend dispatch | 让低精度 dtype 与 backend guard 显式 | #33179 修正 ROCm gfx950 FP8 dtype |
| KV identity cleanup | 清理 stale block、metadata tail、adapter/cache key | #39589/#39591、#30931/#31069 |
| Verification hardening | 用 exact equality 或明确 tolerance 防止假阳性 | #43355、#29086 |

## 当前边界

- 本地缺少 issue 评论正文。
- 很多 PR 缺 changed-file 证据。
- 宽泛 pattern hit 不能直接当 root cause。
- 中文化不翻译上游原文证据；证据保持原语言，wiki 解读使用中文。
