# VllmWiki 实现说明

状态：配置参考。作用：记录当前 VllmWiki 实例的技术实现细节。

## 专题覆盖
| 专题 | 入口 | 状态 |
| --- | --- | --- |
| bitwise/deterministic | [curated/bitwise/README.md](curated/bitwise/README.md) | active |

## 数据源
| 数据层 | 路径 | 说明 |
| --- | --- | --- |
| 本地 source layer | `../all/data/targeted/bitwise/` | issue/PR JSON 全文（不进入 Git） |
| 索引 | `indexes/` | 从 source layer 生成的 CSV 索引（不进入 Git） |
| 候选分类 | `candidates/bitwise_ledger.csv` | 已精读分类的条目（进入 Git） |
| 候选笔记 | `candidates/notes/` | 每个 ledger 条目的精读笔记（进入 Git） |

## 脚本
| 脚本 | 作用 | 触发方式 |
| --- | --- | --- |
| `scripts/run_vllmwiki_iteration.py` | 运行完整迭代并生成 audit 报告 | 手动 |
| `scripts/validate_vllmwiki.py` | 校验结构、链接、ledger 和证据索引 | 手动/CI |
| `scripts/generate_vllm_wiki.py` | 从 source layer 生成 wiki 页面骨架 | 迭代 |
| `scripts/generate_bitwise_review_queue.py` | 生成 bitwise review queue | 迭代 |
| `scripts/query_vllmwiki.py` | 查询 wiki 内容 | 手动 |

## 当前迭代状态
参见 `audit/manifest.json` 了解最新覆盖指标。
