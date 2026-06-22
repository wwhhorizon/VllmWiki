# VllmWiki

VllmWiki 是一个从 vLLM issue/PR 中提炼工程机制的中文知识库。

## 仓库内容边界

**公开仓库仅包含**：
- ` curated/ `：稳定机制页，每条结论须有上游证据链
- ` candidates/ `：候选 note（状态记录、决策依据）与 ledger
- ` docs/ `：维护规则、agent loop 规范、术语表
- ` scripts/ `：验证器、迭代 runner、证据抽取等工具脚本
- ` .github/workflows/ `：CI 治理检查

**公开仓库不包含**：
- raw evidence、source layer、私有数据
- artifacts、generated 层、临时审计产物
- 本地实验日志、模型输出

完整维护规则见 [docs/maintenance.md](docs/maintenance.md)。

## 读者入口

- bitwise / deterministic 机制入口：[curated/bitwise/README.md](curated/bitwise/README.md)
- 稳定机制页：[curated/bitwise/](curated/bitwise/)
- 当前未闭环队列：[curated/bitwise/next.md](curated/bitwise/next.md)

## 维护者入口

- 维护规则：[docs/maintenance.md](docs/maintenance.md)
- Agent loop：[docs/agent_loop.md](docs/agent_loop.md)
- 术语表：[docs/glossary.md](docs/glossary.md)
