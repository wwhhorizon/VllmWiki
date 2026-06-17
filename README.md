# VllmWiki

VllmWiki 是一个从 `vllm-project/vllm` issue 与 PR 语料炼化出的 source-backed 工程知识库。
项目效仿 KernelWiki 的组织方式，把原始材料拆成 source-adjacent 页面、候选模式、领域导航、curated 机制页、索引和质量门。

## 项目概览

| 项 | 数量 / 状态 |
| --- | ---: |
| 原始 issue JSONL 行数 | 16,243 |
| 去重 issue 数 | 15,818 |
| 原始 PR JSONL 行数 | 28,120 |
| 去重 PR 表行数 | 8,931 |
| Operator/kernel 候选 issue 数 | 7,239 |
| 本地 issue-PR 链接 issue 数 | 1,275 |
| 有评论计数但缺评论正文的 issue 数 | 14,271 |
| Issue 状态 | closed=13,816, open=2,002 |
| Case 分类 | correctness=3,748, performance=1,962, development=1,529 |

## 文件树分工

```text
VllmWiki/
├── cases/                 # 本地生成：每个 issue 的 source-adjacent 页面
├── patterns/              # 自动候选模式页，负责聚类而非定论
├── domains/               # 按 vLLM 子系统组织的导航页
├── curated/               # 人工/agent 复核后的机制知识页
│   └── bitwise/           # bitwise/deterministic 六个机制页
├── candidates/            # 候选 claim ledger，记录 include/defer/exclude
├── data/                  # schema、tag、alias、version claim
├── evidence/              # 本地生成：自动抽取的 evidence 表
├── indexes/               # 本地生成：issue / PR 索引表
├── audit/                 # manifest 与每轮迭代审计报告
└── scripts/               # 生成、查询、验证和迭代脚本
```

## 关键入口

- [BITWISE_DETERMINISTIC.md](BITWISE_DETERMINISTIC.md)：当前重点主线，解释 bitwise/deterministic 的目标、产物和阅读顺序。
- [BITWISE_EVIDENCE_SYNTHESIS.md](BITWISE_EVIDENCE_SYNTHESIS.md)：基于 targeted GitHub evidence 的第一轮 bitwise 机制综合。
- [WIKI_REFINEMENT_FLOW.md](WIKI_REFINEMENT_FLOW.md)：VllmWiki 如何效仿 KernelWiki 做知识炼化。
- [KERNELWIKI_REFINEMENT_NOTES.md](KERNELWIKI_REFINEMENT_NOTES.md)：KernelWiki 的 source/wiki/queries/schema/ledger/validate 构建方式。
- [WIKI_IMPLEMENTATION.md](WIKI_IMPLEMENTATION.md)：当前实现层次与证据规则。
- [QUALITY_GATE.md](QUALITY_GATE.md)：质量门与防偷懒规则。

## 常用命令

```powershell
python scripts\query_vllmwiki.py bitwise --kind issue --limit 5
python scripts\get_page.py 33123 --follow-sources
python scripts\grep_wiki.py "deterministic prefix" --only wiki
python scripts\validate_vllmwiki.py
python scripts\run_vllmwiki_iteration.py
```

## 阅读路线

1. 先从根目录概览文档理解项目结构。
2. 如果关注当前主线，直接进入 [BITWISE_DETERMINISTIC.md](BITWISE_DETERMINISTIC.md)。
3. 查具体 issue 时使用本地 `cases/` 或 `all/data/targeted/bitwise`，查问题族时进入 `patterns/`，查子系统时进入 `domains/`。
4. 只有 `curated/` 和 `candidates/` 中带证据状态的内容才接近可复用知识；自动聚类只作为候选导航。
