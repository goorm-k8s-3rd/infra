# infra

```
[.github/workflows]

CI 설정을 위한 Github Actions 폴더

[eks_cluster]

eks를 통한 클러스터 생성

[logging]

EFK 스택을 이용한 로깅 설정

[monitoring]

Prometheus & Grafana를 이용한 모니터링 설정

[test-frontend]

테스트용 프론트엔드

[web]

web deployment
```

```bash
cd eks-cluster
eksctl create cluster -f create_cluster.yaml
```

eks 클러스터에 접속하시려면 이렇게 하시면 됩니다.
```bash
aws eks update-kubeconfig --region ap-northeast-2 --name book-network
```

rds 접속
```bash
 mysql web-db.crpzp5qoygw6.ap-northeast-2.rds.amazonaws.com -u admin -p
```

비밀번호는 슬랙에 잇어용
