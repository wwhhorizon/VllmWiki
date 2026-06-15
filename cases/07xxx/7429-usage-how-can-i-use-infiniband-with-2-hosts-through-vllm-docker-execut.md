# vllm-project/vllm#7429: [Usage]: How can I use InfiniBand with 2 hosts through vllm docker? Execution failed.

| 字段 | 值 |
| --- | --- |
| Issue | [#7429](https://github.com/vllm-project/vllm/issues/7429) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;fp8;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How can I use InfiniBand with 2 hosts through vllm docker? Execution failed.

### Issue 正文摘录

### Your current environment ``` root@86051:/mnt/cpn-pod# ip addr 1: lo: mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000 link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00 inet 127.0.0.1/8 scope host lo valid_lft forever preferred_lft forever inet6 ::1/128 scope host valid_lft forever preferred_lft forever 2: ens15f0np0: mtu 1500 qdisc mq master bond0 state UP group default qlen 1000 link/ether 02:c1:fe:bb:22:ee brd ff:ff:ff:ff:ff:ff permaddr ec:0d:9a:d9:47:aa altname enp73s0f0np0 3: ens15f1np1: mtu 1500 qdisc mq master bond0 state UP group default qlen 1000 link/ether 02:c1:fe:bb:22:ee brd ff:ff:ff:ff:ff:ff permaddr ec:0d:9a:d9:47:ab altname enp73s0f1np1 4: enx964498447070: mtu 1500 qdisc noop state DOWN group default qlen 1000 link/ether 96:44:98:44:70:70 brd ff:ff:ff:ff:ff:ff 5: bond0: mtu 1500 qdisc noqueue state UP group default qlen 1000 link/ether 02:c1:fe:bb:22:ee brd ff:ff:ff:ff:ff:ff inet6 fe80::c1:feff:febb:22ee/64 scope link valid_lft forever preferred_lft forever 6: ibs37: mtu 2044 qdisc mq state UP group default qlen 256 link/infiniband 00:00:10:29:fe:80:00:00:00:00:00:00:1c:34:da:03:00:51:fb:bc brd 00:ff:ff:ff:ff:12:40:1b:ff:ff:00:00:00:00:00:00:ff:...

## 现有链接修复摘要

#42056 Bump the minor-update group across 1 directory with 142 updates | #42717 Bump the minor-update group across 1 directory with 143 updates | #43505 Bump the minor-update group across 1 directory with 145 updates | #43993 Bump the minor-update group across 1 directory with 147 updates

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: ronment ``` root@86051:/mnt/cpn-pod# ip addr 1: lo: mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000 link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00 inet 127.0.0.1/8 scope host lo valid_lft forever pr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Usage]: How can I use InfiniBand with 2 hosts through vllm docker? Execution failed. usage ### Your current environment ``` root@86051:/mnt/cpn-pod# ip addr 1: lo: mtu 65536 qdisc noqueue state UNKNOWN group default ql...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: to use vllm I want use 2 hosts with 8 x 48G each, to run llama3.1 405B FP8, it works with ethernet, but I don't know how to config ib net. Ray status seems work, but vllm failed to execute. ``` docker run -dit --ipc hos...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: would you like to use vllm I want use 2 hosts with 8 x 48G each, to run llama3.1 405B FP8, it works with ethernet, but I don't know how to config ib net. Ray status seems work, but vllm failed to execute. ``` docker run...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: P8', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42056](https://github.com/vllm-project/vllm/pull/42056) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 142 updates | s.get (<a href="https://redirect.github.com/psf/requests/issues/7429">#7429</a>)</li> <li><a href="https://github.com/psf/requests/commit/a4f9a5999bdb9bf2d6e7c8aa973b28cacb17134f"… |
| [#42717](https://github.com/vllm-project/vllm/pull/42717) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 143 updates | s.get (<a href="https://redirect.github.com/psf/requests/issues/7429">#7429</a>)</li> <li><a href="https://github.com/psf/requests/commit/a4f9a5999bdb9bf2d6e7c8aa973b28cacb17134f"… |
| [#43505](https://github.com/vllm-project/vllm/pull/43505) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 145 updates | s.get (<a href="https://redirect.github.com/psf/requests/issues/7429">#7429</a>)</li> <li><a href="https://github.com/psf/requests/commit/a4f9a5999bdb9bf2d6e7c8aa973b28cacb17134f"… |
| [#43993](https://github.com/vllm-project/vllm/pull/43993) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 147 updates | s.get (<a href="https://redirect.github.com/psf/requests/issues/7429">#7429</a>)</li> <li><a href="https://github.com/psf/requests/commit/a4f9a5999bdb9bf2d6e7c8aa973b28cacb17134f"… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
